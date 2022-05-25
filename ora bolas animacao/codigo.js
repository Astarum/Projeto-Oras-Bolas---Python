
    //Para facilitar a consulta neste código, utilize o seguinte sumário:
    //(só copiar do número até a primeira palavra)
//  1 - Objetos
//  2 - Importação as imagens utilizadas
//  3 - Menu principal
//  4 - Tela de seleção de fases
//  5 - Tela de nova fase
//  6 - Tela de game over
//  7 - Blocos de condições associadas aos cliques do mouse
//  8 - Desenho de todos elementos
//  9 - Movimento das nuvens
//  10 - Movimento da carriola
//  11 - Geração aleatória de boost
//  12 - Geração aleatória de cubos de vida
//  13 - Geração aleatória de penas
//  14 - Geração aleatória de pesos
//  15 - Geração aleatória de tijolos
//  16 - Desenho do score e objetivo
//  17 - Desenho da barra de vida, poder e peso
//  18 - Cálculo de FPS
//  19 - Função principal que engloba a linha do requestAnimationFrame


let canvas = document.getElementById("meuCanvas");
let ctx = canvas.getContext("2d")
const campoX = 9;
const campoY = 6;
//variáveis para fazer o cálculo com relação ao refresh rate do monitor
var fps, intervalo, startTime, agora, depois, tempoPassado;

//variável que guarda o valor da diferença dos framerate superiores a 60 ou inferiores
let ajuste2;





var bolaX = [];
var bolaY = [];
var roboX = [];
var roboY = [];


let objetivoConcluido = false;

fps = 60 //coloque aqui o "refreshrate" do seu monitor - padrão 60hz
if(60/fps != 1){
    ajuste2 = 60/fps
}else{
    ajuste2 = 1;
}
let  ajusteParaFrameRate = 1.8*ajuste2 //parâmetro para ajustar a velocidade do jogo, já que eu fiz em 144hz, porém o padrão é 60hz.

//1 - OBJETOS
let chao = {
    x:0,
    y:canvas.height-50,         //chão
    largura: canvas.width+2,
    altura: 50
}
let robo = {


    x: canvas.width/2,
    y: canvas.height/2,
    proporcaoX: campoX/0.7,
    proporcaoY: campoY/0.7,
        get largura(){
            return (canvas.width/this.proporcaoX);
        },

    get altura(){
        return (canvas.height/this.proporcaoY);   //botao de iniciar jogo
    },

}
let bola = {
    x: canvas.width/2,
    y: canvas.height/2,  //carrinho
    proporcaoX: campoX/0.14,
    proporcaoY: campoY/0.14,
    get largura(){
        return (canvas.width/this.proporcaoX);
    },

    get altura(){
        return (canvas.height/this.proporcaoY);   //botao de iniciar jogo
    },

}


/* Caso queira fazer "peso" único
let pesoPesado = {
    x: 30 + Math.random()*canvas.width - 30,
    y: -20,
    largura:50,
    altura:50,
    velocidade: 1*ajusteParaFrameRate
}*/

let parede = {
    x:0,
    y:0,                        //parede de tijolos - fundo
    largura:canvas.width,
    altura: canvas.height-50
}


////////2 - importação das imagens utilizadas
let imagem_robo = new Image();
imagem_robo.src = 'robo-smallsize.png'; //robo -small size

let imagem_bola = new Image();
imagem_bola.src = 'bola.png'; //tijolo






//Bloco que captura as teclas pressionadas
let teclas = {}
document.addEventListener('keydown',function(evento){
    teclas[evento.keyCode] = true;
})

document.addEventListener('keyup',function(evento){
    delete teclas[evento.keyCode];
})



//8 - Desenho de todos elementos
//Desenho de todos elementos
var file = document.getElementById('inputfile');


var terminado = false;
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


        terminado = true;

    }


    fr.readAsText(file.files[0]);
})
    if (terminado == true){
        console.log(bolaX);
    }

var desenhado = false;
function desenharElementos(){
    ctx.clearRect(0, 0, canvas.width, canvas.height);



    ctx.drawImage(imagem_robo, robo.x, robo.y, robo.largura, robo.altura);
    ctx.drawImage(imagem_bola,bola.x,bola.y,bola.largura,bola.altura);
    desenhado = true;

    //Desenho do carrinho
    /*
    if (robo.esquerda === false && robo.direita === true){

    }else{
        ctx.drawImage(imagem_carrinhoEsquerda, robo.x, robo.y, robo.largura, robo.altura);
    }
    */
    //Desenho do chão


}

//10 - Movimento da carriola
//Variáveis usadas no próximo bloco
let boostSegundo = 0;           //Determina a responsividade da barra de boost e o tempo pressionando o botão de boost
let boostFunciona = true;       //Limita o uso do boost
let pause = false;              //Pausar o jogo
var j = 0;
function movimentoRobo() {

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


    robo.x = (canvas.width/roboX_correto)-robo.largura/2;
    robo.y = canvas.height-(canvas.height/roboY_correto)-robo.altura/2;
    bola.x = -bola.largura/2+(canvas.width/bolaX_correto);
    bola.y = canvas.height-(canvas.height/bolaY_correto)-bola.altura/2;
    j+=1;
    if(j>roboX.length-1){
        j = roboX.length-1;
    }

}


/*
//18 - Cálculo de FPS
function calculoFPS(fps){
    intervalo = 1000 / fps;     //função que determina os parâmetros para o cálculo da taxa de atualização padrão para todos
    depois = Date.now();        //monitores e chama a função que executa as animações
    startTime = depois;
    principal();
}
*/
//19 - Função principal (que englobal a linha do requestAnimationFrame)
let atualizacao = 0;
let contador2 = 0;
function principal(){    ///função que executa as todas as animações
       //parâmetro para determinar o gameover e cortar animações
    requestAnimationFrame(principal)
    console.log(desenhado);
    if (terminado == true){
        desenharElementos();
    }
    if(contador2%10==0){
        console.log(contador2)
        if(desenhado==true){
            movimentoRobo();
        }
    }


    agora = Date.now();                             //Cálculos feitos para fazer com que o framerate não importe na animação,
    tempoPassado = agora - depois;                  //ou seja, uma pessoa com 144hz, vai ter o mesmo número de animações que
    if(tempoPassado > intervalo){                   //alguém com 60hz.
        atualizacao +=1                             //
        depois = agora - (tempoPassado % intervalo); //

        //desenharElementos();
        //movimentoCarrinho();
        /*
        if(fimDeJogo === false && objetivoConcluido === false){
            movimentoBoost();
            movimentoPena();
            barrasVidaEPoder();
            score(fase);
            contador2 = 0
        }else if(fimDeJogo === true){                                                   //executar a linha de gameover
            ctx.clearRect(0,0,canvas.width,canvas.height);
            atualizacao = 0;
            gameover();
        }else if(objetivoConcluido === true){
            ctx.clearRect(0,0,canvas.width,canvas.height);
            atualizacao = 0;
            novaFase();
        }*/
    }
    contador2+=1;
}

principal();
