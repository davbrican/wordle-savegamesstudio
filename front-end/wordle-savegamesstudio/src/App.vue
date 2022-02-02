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
    <div class="box resolution">
      <pre>{{resolution}}</pre>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import VueSession from 'vue-session'
import Vue from 'vue'
Vue.use(VueSession)

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
      this.$session.start();
      if (this.$session.get("sessionSaved")) {
        this.letter = this.$session.get("letter");
        this.text = this.$session.get("text");  
        this.triesNumber = this.$session.get("triesNumber");
        this.greens = this.$session.get("greens");
        this.isCorrect = this.$session.get("isCorrect");
        this.isDone = this.$session.get("isDone");
        this.resolution = this.$session.get("resolution");
      } else {
        this.$session.set("letter", [["letter-space","letter-space","letter-space","letter-space","letter-space"],
                  ["letter-space","letter-space","letter-space","letter-space","letter-space"],
                  ["letter-space","letter-space","letter-space","letter-space","letter-space"],
                  ["letter-space","letter-space","letter-space","letter-space","letter-space"],
                  ["letter-space","letter-space","letter-space","letter-space","letter-space"],
                  ["letter-space","letter-space","letter-space","letter-space","letter-space"]]);
          this.$session.set("text", [["","","","",""],
                ["","","","",""],
                ["","","","",""],
                ["","","","",""],
                ["","","","",""],
                ["","","","",""]]);   
          this.$session.set("triesNumber",0);
          this.$session.set("greens",0);
          this.$session.set("isCorrect",false);
          this.$session.set("isDone",false);
          this.$session.set("sessionSaved",true);
          this.$session.set("resolution",'');
      }
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
                this.greens += 1;
              } else if (element == "naranja") {
                this.letter[this.triesNumber][i] = "letter-mid";
              }
            }

            if (this.greens < 5) {
              this.greens = 0;
              if (this.triesNumber == 5) {
                this.isDone = true;
                this.resolution = "HAS PERDIDO...\n";
                for (let l = 0; l < this.letter.length; l++) {
                  const line = this.letter[l];
                  for (let r = 0; r < line.length; r++) {
                    const element = line[r];
                    if (element == "letter-space") {
                      this.resolution += "⚪";
                    } else if (element == "letter-correct") {
                      this.resolution += "🟢";
                    } else if (element == "letter-mid") {
                      this.resolution += "🟡";
                    } else if (element == "letter-bad") {
                      this.resolution += "⚫";
                    }
                  }
                  this.resolution += "\n";
                }
              }
            } else {
              this.isCorrect = true;
                this.resolution = "¡HAS GANADO!\n";
                for (let l = 0; l < this.letter.length; l++) {
                  const line = this.letter[l];
                  for (let r = 0; r < line.length; r++) {
                    const element = line[r];
                    if (element == "letter-space") {
                      this.resolution += "⚪";
                    } else if (element == "letter-correct") {
                      this.resolution += "🟢";
                    } else if (element == "letter-mid") {
                      this.resolution += "🟡";
                    } else if (element == "letter-bad") {
                      this.resolution += "⚫";
                    }
                  }
                  this.resolution += "\n";
                }
            }


            this.triesNumber++;
            this.loaded = true;

            this.$session.set("letter", this.letter);
            this.$session.set("text", this.text);   
            this.$session.set("triesNumber",this.triesNumber);
            this.$session.set("greens",this.greens);
            this.$session.set("isCorrect",this.isCorrect);
            this.$session.set("isDone",this.isDone);
            this.$session.set("resolution",this.resolution);
            this.$session.set("sessionSaved",true);
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
  font-size: 25px;
  font-family: "Lucida Console";
}
pre {
  font-size: 20px;
  font-family: "Lucida Console";
  font-weight: bold;
}
</style>