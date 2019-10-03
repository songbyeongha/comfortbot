<template>
  <v-content class="chatroom">
    <v-content class="chatlist">
      <v-layout align-center justify-center column fill-height class="atumnMild">
        <!--헤더-->
        <v-layout text-xs-center ma-2 class="header">
          <v-icon large>mdi-robot</v-icon>
        </v-layout>

        <!--메시지창-->
        <v-container column class="white messageBox" id="messageBox">
          <message-card
            :key="msgBox.idx"
            v-for="msgBox in messageBoxs"
            :msg="msgBox.msg"
            :type="msgBox.type"
            :myMsg="msgBox.myMsg"
          ></message-card>
          <v-card v-if="isSend" class="mb-5">
            <div class="loadingBox">
              <v-progress-circular indeterminate color="primary"></v-progress-circular>
            </div>
          </v-card>
        </v-container>

        <!--메시지 입력창-->
        <v-layout justify-center align-center pa-2 class="footer atumnMild">
          <v-text-field
            ref="messageInput"
            placeholder="message"
            solo
            hide-details
            v-model="message"
            @keyup.enter="sendMessage"
            :disabled="isSend"
          ></v-text-field>
          <v-btn text icon class="pl-1" @click="sendMessage">
            <v-icon large>mdi-send-circle</v-icon>
          </v-btn>
        </v-layout>
      </v-layout>
    </v-content>
  </v-content>
</template>

<script>
import axios from "axios";
import messageCard from "./MessageCard.vue";

export default {
  name: "ChatRoom",
  data () {
    return {
      message: " ",
      isSend: false,
      messageBoxs: [],
      idx: 0
    };
  },
  components: {
    "message-card": messageCard
  },
  methods: {
    async sendMessage () {
      let container = this.$el.querySelector("#messageBox");
      // 1. 메시지 삭제
      let userMsg = this.message;
      this.message = " ";
      // 2. 입력불가
      this.isSend = true;
      // 2. 사용자 메시지 카드 출력
      await this.messageBoxs.push({ idx: this.idx++, msg: userMsg, type: false });
      container.scrollTop = container.scrollHeight;
      // 3. 챗봇 메시지 카드 생성 및 스피너 실행

      // 3. 서버로 메시지 보내기
      await axios.get(`http://13.124.216.148:5000/api/getMessage?userMsg=${userMsg}`)
        .then((res) => {
          // 5. 서버로부터 받은 응답 카드 출력
          this.messageBoxs.push({ idx: this.idx++, msg: res.data.answer, type: true, myMsg: userMsg });
        })
        .catch((err) => {
          console.error(err);
        })
        .finally(() => {
          // 6. 입력 가능
          container.scrollTop = container.scrollHeight;
          this.isSend = false;
        });
      this.$refs.messageInput.focus();
    }
  }
};
</script>

<style>
.wrenchBtn {
  position: absolute;
  right: 0;
  bottom: 0;
}

.messageBox {
  height: 80%;
  box-shadow: inset 0px 0px 9px -1px #61290e;
  overflow-x: hidden;
  overflow-y: scroll;
}

.loadingBox {
  text-align: center;
  padding: 12px;
}

.messageBox::-webkit-scrollbar {
  display: none;
}

.footer {
  width: 100%;
}

/* 데스크탑 */
@media (min-width: 480px) {
  .chatroom {
    background-image: url("../../public/img/smartphone.png");
    background-position: center;
    background-size: 660px;
    position: absolute;
    left: 0;
    right: 0;
    top: calc(50% - 330px);
    bottom: 0;
    height: 660px;
  }

  .chatlist {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    margin: 56px auto;
    width: 305px;
    height: 541px;
    border-radius: 2px;
  }
}

/* 대부분의 스마트폰 기기 */
@media (max-width: 480px) {
  .chatroom {
    width: 100%;
    height: 100%;
    margin: 0 auto;
    position: absolute;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    margin: auto;
  }

  .chatlist {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    width: 100%;
    height: 100%;
    background-color: transparent;
  }
}

.atumnDark {
  background-color: #c95920;
}
.atumnMild {
  background-color: #f7b25a;
}
.atumnLight {
  background-color: #fce0b8;
}
</style>
