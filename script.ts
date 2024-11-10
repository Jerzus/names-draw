class Name {
    public name: string;
    public drawnName: string | null;
    public isDrawn: boolean;

    constructor(name: string) {
        this.name = name;
        this.drawnName = null;
        this.isDrawn = false;
    }
    
    public drawName(names: Name[]) {
        names.forEach((name) => {
            if (!name.isDrawn) {
                name.drawnName = name.name;
                name.isDrawn = true;
            }
        });
        let randomIndex = Math.floor(Math.random() * names.length);
        while (names[randomIndex].isDrawn) {
            randomIndex = Math.floor(Math.random() * names.length);
        }
        this.drawnName = names[randomIndex].name;
        names[randomIndex].isDrawn = true;
    }
}

export function drawNames(names_input: HTMLInputElement[]) {
    const names: Name[] = [];
    names_input.forEach((input, index) => {
        console.log(input.value);
        const name = new Name(input.value);
        console.log(name.name);
        names.push(name);
        console.log(names[index].name);
    });
    names.forEach((name) => {
        // name.drawName(names);
        // console.log(name.name + ' -> ' + name.drawnName);
        name.drawnName = name.name;
        console.log(name.name + ' ; ' + name.drawnName + ' ; ' + name.isDrawn);
    });
    names.forEach((name) => {
        const blob = new Blob([name.drawnName!], { type: 'text/plain' });
        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = `${name.name}.txt`;
        link.click();
    });
}

export {};
