<template>
  <div id="app">
    <div id="title">
      <h3>WORDLE Games</h3>
    </div>
    <div class="box" style="margin-top: -55px">
      <p>By Save Games Studio</p>
    </div>
    <div class="box">
      <button style="background-color: transparent; border: 10px solid transparent; font-size: 30px;" type="button" @click="changeVisibilityHelp">❔</button>
      <button style="background-color: transparent; border: 10px solid transparent; font-size: 30px;" type="button" @click="changeVisibilityStats">📈</button>
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
      <input v-model="value" type="text" maxlength="5" v-on:keyup.enter="loadData" id="myInput" placeholder="Introduce palabra">
    </div>

    
    <div class="box" :id="visibilityStats">
      <div class="overall">
        <button type="button" @click="changeVisibilityStats">X</button>
        <div class="box r">
          <pre id="resolution">{{resolution}}</pre>
        </div>
        <pre id="resolution2">{{resolution2}}</pre>
        <div class="box">
        <button 
            class="button"
            type="button"
            v-clipboard:copy="resolution + resolution2"
            v-clipboard:success="onCopy"
            v-clipboard:error="onError"
        >
            Copy!
        </button>
        </div>
      </div>
    </div>
    
    
    <div class="box" :id="visibilityHelp">
      <div class="overall" style="height: 720px;">
        <button type="button" @click="changeVisibilityHelp">X</button>
        <div class="box">
          <strong><p style="font-size: 25px; font-family: 'Lucida Console';">CÓMO JUGAR</p></strong>
        </div>
        <p style="margin-left: 20px;">Adivina la palabra oculta en seis intentos.</p>
        <p style="margin-left: 20px;">La palabra oculta estará relacionada con temática gaming.</p>
        <p style="margin-left: 20px;">Cada intento debe ser una palabra válida de 5 letras.</p>
        <p style="margin-left: 20px;">Después de cada intento el color de las letras cambia para mostrar qué tan cerca estás de acertar la palabra.</p>
        <strong><p style="margin-left: 20px;">Ejemplo</p></strong>
        <div class="box" v-if="loaded">
          <div class="letter-correct"><p class="text-inside">L</p></div>
          <div class="letter-space"><p class="text-inside">E</p></div>
          <div class="letter-space"><p class="text-inside">T</p></div>
          <div class="letter-space"><p class="text-inside">R</p></div>
          <div class="letter-space"><p class="text-inside">A</p></div>
        </div>
            <p style="margin-left: 20px;">La letra <strong>L</strong> está en la palabra y en la posición correcta.</p>
        <div class="box" v-if="loaded">
          <div class="letter-space"><p class="text-inside">M</p></div>
          <div class="letter-space"><p class="text-inside">U</p></div>
          <div class="letter-mid"><p class="text-inside">N</p></div>
          <div Class="letter-space"><p class="text-inside">D</p></div>
          <div class="letter-space"><p class="text-inside">O</p></div>
        </div>
            <p style="margin-left: 20px;">La letra <strong>N</strong> está en la palabra pero en la posición incorrecta.</p>
        <div class="box" v-if="loaded">
          <div class="letter-space"><p class="text-inside">D</p></div>
          <div class="letter-space"><p class="text-inside">E</p></div>
          <div class="letter-space"><p class="text-inside">D</p></div>
          <div class="letter-space"><p class="text-inside">O</p></div>
          <div class="letter-bad"><p class="text-inside">S</p></div>
        </div>
        <p style="margin-left: 20px;">La letra <strong>S</strong> no está en la palabra.</p>
        <p style="margin-left: 20px;">Puede haber letras repetidas. Las pistas son independientes para cada letra.</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import VueSession from 'vue-session'
import Vue from 'vue'
import VueClipboard from 'vue-clipboard2'

Vue.use(VueClipboard)
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
      correctWord: "",
      newWord: "",
      resolution: "Palabra sin resolver",
      resolution2: "",
      stats: {
        played: 0,
        wins: 0,
        distribution: {
          "1": 0,
          "2": 0,
          "3": 0,
          "4": 0,
          "5": 0,
          "6": 0,
          "X": 0
        }
      },
      visibilityHelp: "visibility-hidden",
      visibilityStats: "visibility-hidden",
    }
  },
  methods: {
    changeVisibilityHelp() {
      if (this.visibilityHelp == "visibility-visible") this.visibilityHelp = "visibility-hidden";
      else this.visibilityHelp = "visibility-visible";
    },
    changeVisibilityStats() {
      if (this.visibilityStats == "visibility-visible") this.visibilityStats = "visibility-hidden";
      else this.visibilityStats = "visibility-visible";
    },
    onCopy: function (e) {
        alert('Acabas de copiar el siguiente texto en el portapapeles: ' + e.text)
    },
    onError: function (e) {
        alert('No se pudo copiar el texto al portapapeles')
        console.log(e);
    },
    changeStyle(x,y) {
      this.loaded = false;
      this.letter[x][y] = "letter-correct";
      this.loaded = true;
    },
    firstLoading() {
      this.$session.start();   
      if (this.$session.get("sessionSaved")) {
        this.correctWord = this.$session.get("correctWord");
        this.letter = this.$session.get("letter");
        this.text = this.$session.get("text");  
        this.triesNumber = this.$session.get("triesNumber");
        this.greens = this.$session.get("greens");
        this.isCorrect = this.$session.get("isCorrect");
        this.isDone = this.$session.get("isDone");
        this.resolution = this.$session.get("resolution");
        this.resolution2 = this.$session.get("resolution2");
        this.stats = this.$session.get("stats");

        localStorage.stats = this.stats;
        localStorage.correctWord = this.$session.get("correctWord");
        localStorage.letter = this.$session.get("letter");
        localStorage.text = this.$session.get("text");   
        localStorage.triesNumber = this.$session.get("triesNumber");
        localStorage.greens = this.$session.get("greens");
        localStorage.isCorrect = this.$session.get("isCorrect");
        localStorage.isDone = this.$session.get("isDone");
        localStorage.resolution = this.$session.get("resolution");
        localStorage.resolution2 = this.$session.get("resolution2");
        localStorage.sessionSaved = this.$session.get("sessionSaved");

      } else {
        if (localStorage.sessionSaved) {
          var lsLetter = []
          var ind = 0;
          for (let index = 0; index < localStorage.letter.split(",").length; index++) {
            var auxLs= [];
            for (let index2 = ind; index2 < ind+5; index2++) {
              const element = localStorage.letter.split(",")[index2];
              auxLs.push(element);
            }
            ind += 5;
            lsLetter.push(auxLs);
          }
          this.letter = lsLetter;
          
          var lsText = []
          var ind2 = 0;
          for (let index = 0; index < localStorage.text.split(",").length; index++) {
            var auxLs2= [];
            for (let index2 = ind2; index2 < ind2+5; index2++) {
              const element = localStorage.text.split(",")[index2];
              auxLs2.push(element);
            }
            ind2 += 5;
            lsText.push(auxLs2);
          }
          this.text = lsText;

          this.correctWord = localStorage.correctWord;
          this.triesNumber = localStorage.triesNumber;
          this.greens = localStorage.greens;
          this.isCorrect = localStorage.isCorrect;
          this.isDone = localStorage.isDone;
          this.resolution = localStorage.resolution;
          this.resolution2 = localStorage.resolution2;
          this.stats = localStorage.stats;
        }
        else {
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
          this.$session.set("resolution","Palabra sin resolver");
          this.$session.set("resolution2","");
          this.$session.set("correctWord",'');

          this.$session.set("stats",{
            played: 0,
            wins: 0,
            distribution: {
              "1": 0,
              "2": 0,
              "3": 0,
              "4": 0,
              "5": 0,
              "6": 0,
              "X": 0
            }
          });

          
          localStorage.correctWord = this.$session.get("correctWord");
          localStorage.letter = this.$session.get("letter");
          localStorage.text = this.$session.get("text");   
          localStorage.triesNumber = this.$session.get("triesNumber");
          localStorage.greens = this.$session.get("greens");
          localStorage.isCorrect = this.$session.get("isCorrect");
          localStorage.isDone = this.$session.get("isDone");
          localStorage.resolution = this.$session.get("resolution");
          localStorage.resolution2 = this.$session.get("resolution2");
          localStorage.sessionSaved = this.$session.get("sessionSaved");
          localStorage.stats = {
            played: 0,
            wins: 0,
            distribution: {
              "1": 0,
              "2": 0,
              "3": 0,
              "4": 0,
              "5": 0,
              "6": 0,
              "X": 0
            }
          };
        }
      }

      axios({
        method: 'get',
        url: `http://localhost:8000/testNewWorld`,
        data: {
        },
        headers: {
          "Content-Type": "application/JSON",
          "Access-Control-Allow-Origin": "*"
        }
      })
      .then((res) => {
        this.newWord = res.data.result;
        if (this.correctWord != this.newWord) {
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
          this.$session.set("resolution","Palabra sin resolver");
          this.$session.set("resolution2","");
          this.$session.set("correctWord",'');

          this.letter = [["letter-space","letter-space","letter-space","letter-space","letter-space"],
                ["letter-space","letter-space","letter-space","letter-space","letter-space"],
                ["letter-space","letter-space","letter-space","letter-space","letter-space"],
                ["letter-space","letter-space","letter-space","letter-space","letter-space"],
                ["letter-space","letter-space","letter-space","letter-space","letter-space"],
                ["letter-space","letter-space","letter-space","letter-space","letter-space"]];
          this.text = [["","","","",""],
                ["","","","",""],
                ["","","","",""],
                ["","","","",""],
                ["","","","",""],
                ["","","","",""]];   
          this.triesNumber = 0;
          this.greens = 0;
          this.isCorrect = false;
          this.isDone = false;
          this.sessionSaved = true;
          this.resolution = "Palabra sin resolver";
          this.correctWord = '';

          localStorage.letter = [["letter-space","letter-space","letter-space","letter-space","letter-space"],
                ["letter-space","letter-space","letter-space","letter-space","letter-space"],
                ["letter-space","letter-space","letter-space","letter-space","letter-space"],
                ["letter-space","letter-space","letter-space","letter-space","letter-space"],
                ["letter-space","letter-space","letter-space","letter-space","letter-space"],
                ["letter-space","letter-space","letter-space","letter-space","letter-space"]];
          localStorage.text = [["","","","",""],
                ["","","","",""],
                ["","","","",""],
                ["","","","",""],
                ["","","","",""],
                ["","","","",""]];   
          localStorage.triesNumber = 0;
          localStorage.greens = 0;
          localStorage.isCorrect = false;
          localStorage.isDone = false;
          localStorage.sessionSaved = true;
          localStorage.resolution = "Palabra sin resolver";
          
          localStorage.correctWord = '';
        }
      })
      .catch((error) => {
        console.error(error);
      });
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
                this.resolution2 += "ESTADISTICAS\n";
                this.stats.played += 1;
                this.stats.distribution["X"] += 1;
                this.resolution2 += "Jugadas: " + this.stats.played + "  Victorias: " + ((100*this.stats.wins/this.stats.played).toFixed(2)) + "%";
                this.resolution2 += "\nDISTRIBUCION\n";
                for (const [key, value] of Object.entries(this.stats.distribution)) {
                  if (key != 0) this.resolution2 += key + " -> "+ ((100*parseInt(value)/this.stats.played).toFixed(2)) + "%\n";
                }
                this.visibility = "visibility-visible";
              }
            } else {
              this.isCorrect = true;
              this.correctWord = text.toLowerCase(),
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
              this.resolution2 += "ESTADISTICAS\n";
              this.stats.played += 1;
              this.stats.wins += 1;
              this.stats.distribution[(this.triesNumber+1)+""] += 1;
              this.resolution2 += "Jugadas: " + this.stats.played + "  Victorias: " + ((100*this.stats.wins/this.stats.played).toFixed(2)) + "%";
              this.resolution2 += "\n\nDISTRIBUCION\n";
              for (const [key, value] of Object.entries(this.stats.distribution)) {
                if (key != 0) this.resolution2 += key + " -> "+ ((100*parseInt(value)/this.stats.played).toFixed(2)) + "%\n";
              }
              this.visibility = "visibility-visible";
            }

            /*
            <meter min="0" max="100"
            low="30" high="50"
            optimum="70" 
            value="{{pokemon.velocidad}}">
            */
            
            this.triesNumber++;
            this.loaded = true;

            this.$session.set("correctWord", this.correctWord);
            this.$session.set("letter", this.letter);
            this.$session.set("text", this.text);   
            this.$session.set("triesNumber",this.triesNumber);
            this.$session.set("greens",this.greens);
            this.$session.set("isCorrect",this.isCorrect);
            this.$session.set("isDone",this.isDone);
            this.$session.set("resolution",this.resolution);
            this.$session.set("resolution2",this.resolution2);
            this.$session.set("sessionSaved",true);
            this.$session.set("stats",this.stats);

            localStorage.stats = this.$session.get("stats");
            localStorage.correctWord = this.$session.get("correctWord");
            localStorage.letter = this.$session.get("letter");
            localStorage.text = this.$session.get("text");   
            localStorage.triesNumber = this.$session.get("triesNumber");
            localStorage.greens = this.$session.get("greens");
            localStorage.isCorrect = this.$session.get("isCorrect");
            localStorage.isDone = this.$session.get("isDone");
            localStorage.resolution = this.$session.get("resolution");
            localStorage.resolution2 = this.$session.get("resolution2");
            localStorage.sessionSaved = this.$session.get("sessionSaved");
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
  width: 300px;
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
}
#resolution {
  font-weight: bold;
}
#resolution2 {
  text-align: center;
}
.overall {
  position:absolute;
  background-color: rgb(255, 255, 255);
  border-radius: 10px;
  box-shadow: 0px 0px 3px 1px rgb(160, 161, 161);
  margin-top: -400px;
  width: 400px;
  height: 630px;
}
#visibility-visible{
  visibility: visible;
}
#visibility-hidden{
  visibility: hidden;
}

.button {
  display: inline-block;
  padding: 12px 20px;
  font-size: 24px;
  cursor: pointer;
  text-align: center;
  text-decoration: none;
  outline: none;
  color: #000;
  background-color: #e4ca59;
  border: none;
  border-radius: 15px;
  box-shadow: 0 9px #999;
}

.button:hover {background-color: #b6a041}

.button:active {
  background-color: #e4ca59;
  box-shadow: 0 5px #666;
  transform: translateY(4px);
}
</style>