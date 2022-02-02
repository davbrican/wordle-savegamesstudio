<template>
  <div id="app">
    <div id="title">
      <h3>WORDLE (SaveGamesStudio)</h3>
    </div>
    <br>
    <div class="box 1" v-if="loaded">
      <div :class="letter[0][0]" @click="changeStyle(0,0)"><p class="text-inside">{{text[0][0]}}</p></div>
      <div :class="letter[0][1]" @click="changeStyle(0,1)"><p class="text-inside">{{text[0][1]}}</p></div>
      <div :class="letter[0][2]" @click="changeStyle(0,2)"><p class="text-inside">{{text[0][2]}}</p></div>
      <div :class="letter[0][3]" @click="changeStyle(0,3)"><p class="text-inside">{{text[0][3]}}</p></div>
      <div :class="letter[0][4]" @click="changeStyle(0,4)"><p class="text-inside">{{text[0][4]}}</p></div>
    </div>
    <div class="box 2" v-if="loaded">
      <div :class="letter[1][0]" @click="changeStyle(1,0)"><p class="text-inside">{{text[1][0]}}</p></div>
      <div :class="letter[1][1]" @click="changeStyle(1,1)"><p class="text-inside">{{text[1][1]}}</p></div>
      <div :class="letter[1][2]" @click="changeStyle(1,2)"><p class="text-inside">{{text[1][2]}}</p></div>
      <div :class="letter[1][3]" @click="changeStyle(1,3)"><p class="text-inside">{{text[1][3]}}</p></div>
      <div :class="letter[1][4]" @click="changeStyle(1,4)"><p class="text-inside">{{text[1][4]}}</p></div>
    </div>
    <div class="box 3" v-if="loaded">
      <div :class="letter[2][0]" @click="changeStyle(2,0)"><p class="text-inside">{{text[2][0]}}</p></div>
      <div :class="letter[2][1]" @click="changeStyle(2,1)"><p class="text-inside">{{text[2][1]}}</p></div>
      <div :class="letter[2][2]" @click="changeStyle(2,2)"><p class="text-inside">{{text[2][2]}}</p></div>
      <div :class="letter[2][3]" @click="changeStyle(2,3)"><p class="text-inside">{{text[2][3]}}</p></div>
      <div :class="letter[2][4]" @click="changeStyle(2,4)"><p class="text-inside">{{text[2][4]}}</p></div>
    </div>
    <div class="box 4" v-if="loaded">
      <div :class="letter[3][0]" @click="changeStyle(3,0)"><p class="text-inside">{{text[3][0]}}</p></div>
      <div :class="letter[3][1]" @click="changeStyle(3,1)"><p class="text-inside">{{text[3][1]}}</p></div>
      <div :class="letter[3][2]" @click="changeStyle(3,2)"><p class="text-inside">{{text[3][2]}}</p></div>
      <div :class="letter[3][3]" @click="changeStyle(3,3)"><p class="text-inside">{{text[3][3]}}</p></div>
      <div :class="letter[3][4]" @click="changeStyle(3,4)"><p class="text-inside">{{text[3][4]}}</p></div>
    </div>
    <div class="box 5" v-if="loaded">
      <div :class="letter[4][0]" @click="changeStyle(4,0)"><p class="text-inside">{{text[4][0]}}</p></div>
      <div :class="letter[4][1]" @click="changeStyle(4,1)"><p class="text-inside">{{text[4][1]}}</p></div>
      <div :class="letter[4][2]" @click="changeStyle(4,2)"><p class="text-inside">{{text[4][2]}}</p></div>
      <div :class="letter[4][3]" @click="changeStyle(4,3)"><p class="text-inside">{{text[4][3]}}</p></div>
      <div :class="letter[4][4]" @click="changeStyle(4,4)"><p class="text-inside">{{text[4][4]}}</p></div>
    </div>
    <div class="box 6" v-if="loaded">
      <div :class="letter[5][0]" @click="changeStyle(5,0)"><p class="text-inside">{{text[5][0]}}</p></div>
      <div :class="letter[5][1]" @click="changeStyle(5,1)"><p class="text-inside">{{text[5][1]}}</p></div>
      <div :class="letter[5][2]" @click="changeStyle(5,2)"><p class="text-inside">{{text[5][2]}}</p></div>
      <div :class="letter[5][3]" @click="changeStyle(5,3)"><p class="text-inside">{{text[5][3]}}</p></div>
      <div :class="letter[5][4]" @click="changeStyle(5,4)"><p class="text-inside">{{text[5][4]}}</p></div>
    </div>
    <div class="box input">
      <input v-model="value" type="text" maxlength="5" v-on:keyup.enter="loadData" id="myInput">
    </div>
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
      value: ''
    }
  },
  methods: {
    changeStyle(x,y) {
      this.loaded = false;
      this.letter[x][y] = "letter-correct";
      this.loaded = true;
    },
    loadData() {
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
          "palabra": text,
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
              this.letter[this.triesNumber][i] = "letter-space";
            } else if (element == "verde") {
              this.letter[this.triesNumber][i] = "letter-correct";
            } else if (element == "naranja") {
              this.letter[this.triesNumber][i] = "letter-mid";
            }
          }
          this.triesNumber++;
          this.loaded = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  mounted() {
    
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
  background-color: rgb(185, 185, 185);
  width: 10px;
  height: 10px;
  border: 2px solid rgb(126, 126, 126);
  padding: 20px;
  margin: 5px;
}
.letter-correct {
  background-color: rgb(141, 241, 149);
  width: 10px;
  height: 10px;
  border: 2px solid rgb(0, 121, 26);
  padding: 20px;
  margin: 5px;
}
.letter-mid {
  background-color: rgb(241, 223, 141);
  width: 10px;
  height: 10px;
  border: 2px solid rgb(207, 125, 30);
  padding: 20px;
  margin: 5px;
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