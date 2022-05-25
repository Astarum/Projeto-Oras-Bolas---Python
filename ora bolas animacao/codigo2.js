var file = document.getElementById('inputfile');

var bolaX = [];
var bolaY = [];
var roboX = [];
var roboY = [];
var renderizado = false;
file.addEventListener('change', () => {

    var fr = new FileReader();
    fr.onload = function() {

        var lines = this.result.split('\n');

        for(var i=0;i<lines.length;i++){
            if (lines[i]!=""){
                dividido = lines[i].split(" ");
                //console.log(dividido[0]);

                bolaX.push(parseFloat(dividido[1]));
                bolaY.push(parseFloat(dividido[2]));
                roboX.push(parseFloat(dividido[3]));
                roboY.push(parseFloat(dividido[4]));
            }
        }


        renderizado = true;

        console.log(bolaX);
    }


    fr.readAsText(file.files[0]);
})
if (renderizado == true){

}
