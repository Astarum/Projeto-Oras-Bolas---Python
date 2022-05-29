let canvas = document.getElementById("meuCanvas");
let ctx = canvas.getContext("2d")
//tamanho do campo
const campoX = 9;
const campoY = 6;


//listas da bola, do robo e do tempo
var bolaX = [];
var bolaY = [];
var roboX = [];
var roboY = [];
var  tempo = []




let robo = {


    x: canvas.width/2,
    y: canvas.height/2,
    proporcaoX: campoX/0.8,
    proporcaoY: campoY/0.8,
        get largura(){
            return (canvas.width/this.proporcaoX);
        },

    get altura(){
        return (canvas.height/this.proporcaoY);   //propriedades do robo
    },

}
let bola = {
    x: canvas.width/2,
    y: canvas.height/2,  //carrinho
    proporcaoX: campoX/0.30,
    proporcaoY: campoY/0.30,
    get largura(){
        return (canvas.width/this.proporcaoX);
    },

    get altura(){
        return (canvas.height/this.proporcaoY);   //propriedades da bola
    },

}



let campo = {
    x:-65,
    y:-15,                        //propriedades do campo
    largura:canvas.width+131,
    altura: canvas.height+30,
}


//////// importação das imagens utilizadas
let imagem_robo = new Image();
imagem_robo.src = 'robo-smallsize.png'; //robo -small size

let imagem_bola = new Image();
imagem_bola.src = 'bola.png';

let imagem_campo = new Image();
imagem_campo.src = 'campo.jpeg';



//pega as informações do arquivo e guarda nas listas
var file = document.getElementById('escolher_arquivo');



var terminado = false;
file.addEventListener('change', () => {

    var fr = new FileReader();
    fr.onload = function() {
        //le o arquivo e cria uma lista com as linhas
        var linhas = this.result.split('\n');

        //atribui cada valor da linha à lista correta
        for(var i=0;i<linhas.length;i++){
            if (linhas[i]!=""){
                dividido = linhas[i].split(" ");
                //console.log(dividido[0]);

                bolaX.push(parseFloat(dividido[1]));
                bolaY.push(parseFloat(dividido[2]));
                roboX.push(parseFloat(dividido[3]));
                roboY.push(parseFloat(dividido[4]));
                tempo.push(parseFloat(dividido[0]));

            }
        }

        //termina o processo
        terminado = true;

    }


    fr.readAsText(file.files[0]);
})
    if (terminado == true){
        console.log(bolaX);
    }

//variável que bloqueia o desenho das figuras
var desenhado = false;
var fim_animacao = false;
var frase;

//desenha o campo
 function desenharCampo(){

     ctx.drawImage(imagem_campo,campo.x,campo.y,campo.largura,campo.altura);

 }

//desenha todos os outros elementos
function desenharElementos(){
    ctx.clearRect(0, 0, canvas.width, canvas.height);


    ctx.drawImage(imagem_campo,campo.x,campo.y,campo.largura,campo.altura);
    ctx.drawImage(imagem_robo, robo.x, robo.y, robo.largura, robo.altura);
    ctx.drawImage(imagem_bola,bola.x,bola.y,bola.largura,bola.altura);

    if (fim_animacao == false){
        if (pause == false){
            ctx.fillStyle = "black";
            ctx.textAlign = 'center';
            ctx.font = "45px Arial";

            ctx.fillText(tempo[j], canvas.width/2, (canvas.height)/2-300);
        }else{
            ctx.fillStyle = "white";
            ctx.font = "40px Arial";
            ctx.fillText(`Instante de tempo: ${tempo[j]}`, canvas.width/2, (canvas.height)/2);
            ctx.fillText(`Posição do robô: X:${roboX[j]} Y:${roboY[j]}`, canvas.width/2, (canvas.height)/2+50);
            ctx.fillText(`Posição da bola: X:${bolaX[j]} Y:${bolaY[j]}`, canvas.width/2, (canvas.height)/2+100);

        }

    }
    else{
        ctx.fillStyle = "white";
        ctx.textAlign = 'center';
        ctx.font = "70px Arial";

        ctx.fillText("Bola interceptada!!!", canvas.width/2, (canvas.height)/2-100);

        ctx.font = "40px Arial";
        ctx.fillText(`Instante de tempo: ${tempo[j]}`, canvas.width/2, (canvas.height)/2);
        ctx.fillText(`Posição do robô: X:${roboX[j]} Y:${roboY[j]}`, canvas.width/2, (canvas.height)/2+50);
        ctx.fillText(`Posição da bola: X:${bolaX[j]} Y:${bolaY[j]}`, canvas.width/2, (canvas.height)/2+100);




    }


    desenhado = true;



}


//variável para contar os indices das listas
var j = 0;

//atribui movimento ao robo e abola
function movimentoRoboBola() {

/*
    robo.x = canvas.width/2-robo.largura/2-canvas.width*0.001;
    robo.y = canvas.height/2-robo.altura/2;
    bola.x = canvas.width/2-bola.largura/2;
    bola.y = canvas.height/2-bola.altura/2;
    */

    var roboX_correto = campoX/roboX[j];
    var roboY_correto = campoY/roboY[j];
    var bolaX_correto = campoX/bolaX[j];
    var bolaY_correto = campoY/bolaY[j];

    //cria a função do pause, só executa se não estiver pausado
    if (pause == false){

        robo.x = (canvas.width/roboX_correto)-robo.largura/2;
        robo.y = canvas.height-(canvas.height/roboY_correto)-robo.altura/2;
        bola.x = -bola.largura/2+(canvas.width/bolaX_correto);
        bola.y = canvas.height-(canvas.height/bolaY_correto)-bola.altura/2;
        j+=1;

        if(j>roboX.length-1){
            j = roboX.length-1;
            fim_animacao = true;
        }
    }



}



//contador para controlar a velocidade da animação
let contador2 = 0;

///função que executa as todas as animações
function principal(){

    requestAnimationFrame(principal)
    desenharCampo();


    //só desenha se já tiver terminado de pegar todas informações do arquivo
    if (terminado == true){
        desenharElementos();
    }
    //controla a velocidade da animação, quanto maior o valor, mais lenta a animação
    if(contador2%8==0){

        if(desenhado==true){
            movimentoRoboBola();

        }

    }



    contador2+=1;
}

//controlar o pause
let pause = false;
function pausar(){
    if (pause == false){
        pause = true;
    }else{
        pause = false;
    }

}



//botao de iniciar
function iniciar(){
        principal();


}

