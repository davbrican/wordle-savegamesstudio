<template>
  <div id="app">
    <div id="title">
      <h3>WORDLE (SaveGamesStudio)</h3>
    </div>
    <br>
    <div class="box 1" v-if="loaded">
      <div :class="letter[0][0]"><p class="text-inside">{{text[0][0]}}</p></div>
      <div :class="letter[0][1]"><p class="text-inside">{{text[0][1]}}</p></div>
      <div :class="letter[0][2]"><p class="text-inside">{{text[0][2]}}</p></div>
      <div :class="letter[0][3]"><p class="text-inside">{{text[0][3]}}</p></div>
      <div :class="letter[0][4]"><p class="text-inside">{{text[0][4]}}</p></div>
    </div>
    <div class="box 2" v-if="loaded">
      <div :class="letter[1][0]"><p class="text-inside">{{text[1][0]}}</p></div>
      <div :class="letter[1][1]"><p class="text-inside">{{text[1][1]}}</p></div>
      <div :class="letter[1][2]"><p class="text-inside">{{text[1][2]}}</p></div>
      <div :class="letter[1][3]"><p class="text-inside">{{text[1][3]}}</p></div>
      <div :class="letter[1][4]"><p class="text-inside">{{text[1][4]}}</p></div>
    </div>
    <div class="box 3" v-if="loaded">
      <div :class="letter[2][0]"><p class="text-inside">{{text[2][0]}}</p></div>
      <div :class="letter[2][1]"><p class="text-inside">{{text[2][1]}}</p></div>
      <div :class="letter[2][2]"><p class="text-inside">{{text[2][2]}}</p></div>
      <div :class="letter[2][3]"><p class="text-inside">{{text[2][3]}}</p></div>
      <div :class="letter[2][4]"><p class="text-inside">{{text[2][4]}}</p></div>
    </div>
    <div class="box 4" v-if="loaded">
      <div :class="letter[3][0]"><p class="text-inside">{{text[3][0]}}</p></div>
      <div :class="letter[3][1]"><p class="text-inside">{{text[3][1]}}</p></div>
      <div :class="letter[3][2]"><p class="text-inside">{{text[3][2]}}</p></div>
      <div :class="letter[3][3]"><p class="text-inside">{{text[3][3]}}</p></div>
      <div :class="letter[3][4]"><p class="text-inside">{{text[3][4]}}</p></div>
    </div>
    <div class="box 5" v-if="loaded">
      <div :class="letter[4][0]"><p class="text-inside">{{text[4][0]}}</p></div>
      <div :class="letter[4][1]"><p class="text-inside">{{text[4][1]}}</p></div>
      <div :class="letter[4][2]"><p class="text-inside">{{text[4][2]}}</p></div>
      <div :class="letter[4][3]"><p class="text-inside">{{text[4][3]}}</p></div>
      <div :class="letter[4][4]"><p class="text-inside">{{text[4][4]}}</p></div>
    </div>
    <div class="box 6" v-if="loaded">
      <div :class="letter[5][0]"><p class="text-inside">{{text[5][0]}}</p></div>
      <div :class="letter[5][1]"><p class="text-inside">{{text[5][1]}}</p></div>
      <div :class="letter[5][2]"><p class="text-inside">{{text[5][2]}}</p></div>
      <div :class="letter[5][3]"><p class="text-inside">{{text[5][3]}}</p></div>
      <div :class="letter[5][4]"><p class="text-inside">{{text[5][4]}}</p></div>
    </div>
    <div class="box input">
      <input v-model="value" type="text" maxlength="5" v-on:keyup.enter="loadData" id="myInput">
    </div>
    {{resolution}}
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      letter: [["letter-space","letter-space","letter-space","letter-space","letter-space"],
              ["letter-space","letter-space","letter-space","letter-space","letter-space"],
              ["letter-space","letter-space","letter-space","letter-space","letter-space"],
              ["letter-space","letter-space","letter-space","letter-space","letter-space"],
              ["letter-space","letter-space","letter-space","letter-space","letter-space"],
              ["letter-space","letter-space","letter-space","letter-space","letter-space"]],
      loaded: true,
      text: [["","","","",""],
            ["","","","",""],
            ["","","","",""],
            ["","","","",""],
            ["","","","",""],
            ["","","","",""]],
      triesNumber: 0,
      value: '',
      greens: 0,
      isCorrect: false,
      isDone: false,
      resolution: ''
    }
  },
  methods: {
    changeStyle(x,y) {
      this.loaded = false;
      this.letter[x][y] = "letter-correct";
      this.loaded = true;
    },
    firstLoading() {
      
    },
    loadData() {
      if(this.greens < 5 && this.triesNumber < 6) {
        var text = document.getElementById("myInput").value;
        for (let j = 0; j < text.split("").length; j++) {
          var element = text.split("")[j];
          this.text[this.triesNumber][j] = element.toUpperCase();
        }
        const path = `http://localhost:8000/testWord`;
        const config = {
          method: 'post',
          url: path,
          data: {
            "palabra": text.toLowerCase(),
            "numero_intentos": this.triesNumber
          },
          headers: {
            "Content-Type": "application/JSON",
            "Access-Control-Allow-Origin": "*"
          }
        };
        axios(config)
          .then((res) => {
            this.loaded = false;
            var lista_resultados = res.data.result;

            for (let i = 0; i < lista_resultados.length; i++) {
              const element = lista_resultados[i];
              if (element == "gris") {
                this.letter[this.triesNumber][i] = "letter-bad";
              } else if (element == "verde") {
                this.letter[this.triesNumber][i] = "letter-correct";
                this.greens++;
              } else if (element == "naranja") {
                this.letter[this.triesNumber][i] = "letter-mid";
              }
            }

            if (this.greens < 5) {
              this.greens = 0;
              if (this.triesNumber == 5) {
                this.isDone = true;
                this.resolution = "HAS PERDIDO!";
              }
            } else {
              this.isCorrect = true;
                this.resolution = "HAS GANADO!";
            }


            this.triesNumber++;
            this.loaded = true;
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
      }
    },
  },
  mounted() {
    this.firstLoading();
  }
};
</script>

<style>
#title {
  font-size: 30px;
  font-weight: bold;
  text-align: center;
}
.letter-space {
  background-color: rgb(255, 255, 255);
  width: 10px;
  height: 10px;
  border: 2px solid rgb(212, 212, 212);
  padding: 20px;
  margin: 5px;
  border-radius: 10px;
}
.letter-correct {
  background-color: rgb(141, 241, 149);
  width: 10px;
  height: 10px;
  border: 2px solid rgb(0, 121, 26);
  padding: 20px;
  margin: 5px;
  border-radius: 10px;
}
.letter-mid {
  background-color: rgb(241, 223, 141);
  width: 10px;
  height: 10px;
  border: 2px solid rgb(207, 125, 30);
  padding: 20px;
  margin: 5px;
  border-radius: 10px;
}
.letter-bad {
  background-color: rgb(160, 160, 160);
  width: 10px;
  height: 10px;
  border: 2px solid rgb(114, 114, 114);
  padding: 20px;
  margin: 5px;
  border-radius: 10px;
}
.box {
  display: flex;
  align-items: center;
  justify-content: center;
}
.text-inside {
  font-size: 25px;
  font-weight: bold;  
  margin-top: -9px; 
  margin-left: -4px;
  font-family: "Lucida Console";
}
#myInput {
  width: 20%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}
</style>