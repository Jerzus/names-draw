"use strict";
exports.__esModule = true;
exports.drawNames = void 0;
var Name = /** @class */ (function () {
    function Name(name) {
        this.name = name;
        this.drawnName = null;
        this.isDrawn = false;
    }
    Name.prototype.drawName = function (names) {
        names.forEach(function (name) {
            if (!name.isDrawn) {
                name.drawnName = name.name;
                name.isDrawn = true;
            }
        });
        var randomIndex = Math.floor(Math.random() * names.length);
        while (names[randomIndex].isDrawn) {
            randomIndex = Math.floor(Math.random() * names.length);
        }
        this.drawnName = names[randomIndex].name;
        names[randomIndex].isDrawn = true;
    };
    return Name;
}());
function drawNames(names_input) {
    var names = [];
    names_input.forEach(function (input, index) {
        console.log(input.value);
        var name = new Name(input.value);
        console.log(name.name);
        names.push(name);
        console.log(names[index].name);
    });
    names.forEach(function (name) {
        // name.drawName(names);
        // console.log(name.name + ' -> ' + name.drawnName);
        name.drawnName = name.name;
        console.log(name.name + ' ; ' + name.drawnName + ' ; ' + name.isDrawn);
    });
    names.forEach(function (name) {
        var blob = new Blob([name.drawnName], { type: 'text/plain' });
        var link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = "".concat(name.name, ".txt");
        link.click();
    });
}
exports.drawNames = drawNames;
