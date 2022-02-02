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
  </div>
</template>

<script>
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
            ["","","","",""]]
    }
  },
  methods: {
    changeStyle(x,y) {
      this.loaded = false;
      this.letter[x][y] = "letter-correct";
      this.loaded = true;
    }
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
</style>