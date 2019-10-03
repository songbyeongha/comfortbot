<template>
  <v-card class="mb-5" :class="isBot()">
    <v-card-title primary-title>
      <div>
        <div>{{ msg }}</div>
      </div>
    </v-card-title>
    <v-card-actions v-if="type">
      <v-btn text icon color="#c95920" class="white--text wrenchBtn" @click="showAlert" >
        <v-icon color="green">mdi-progress-wrench</v-icon>
      </v-btn>
    </v-card-actions>
	  <v-snackbar color="#b3d4fc" text-color="black" v-model="snackbar">
      {{ snacktext }}
      <v-btn color="black" text @click="snackbar = false">
        Close
      </v-btn>
    </v-snackbar>
  </v-card>
</template>

<script>
import axios from "axios";
import Swal from 'sweetalert2'

export default {
  props: {
    type: { type: Boolean },
    msg: { type: String },
    myMsg: { type: String }
  },
  data: () => ({
      snackbar: false,
      snacktext: '빈칸을 채워주세요'
  }),
 
  methods: {
    isBot() {
      if(this.type) {
        return "";
      } else {
        return "msgUser";
      }
    },
    showAlert() {
			const swalWithBootstrapButtons = Swal.mixin({
				customClass: {
					confirmButton: 'btn btn-success',
					cancelButton: 'btn btn-danger'
				},
				buttonsStyling: true
			})

			swalWithBootstrapButtons.fire({
				title: 'Are you sure?',
				text: "수정 요청하겠습니까?",
				input:'text',
				type: 'warning',
				showCancelButton: true,
				confirmButtonText: 'Yes, Send it!',
				cancelButtonText: 'No, cancel!',
				reverseButtons: true
			})
				.then((result) => {
					if(result.dismiss === Swal.DismissReason.cancel) {
						swalWithBootstrapButtons.fire(
							'Cancelled',
							'Your imaginary file is safe :)',
							'error'
						)
					} else if (result.value.length == 0) {
						this.snackbar = true
					} else if (result.value) {
						let parms={
							question: this.myMsg,
							answer: this.msg,
							change_answer: result.value
						}

						axios.post(`http://13.124.216.148:5000/api/reports`,parms)
							.then((res) => {
								swalWithBootstrapButtons.fire(
									'Send!',
									'Your file has been Send.',
									'success'
								)
							})
							.catch(error => {
								Swal.showValidationMessage(
									`Request failed: ${error}`
								)
							})
					}
				})
    }
  }
};
</script>

<style scope>
.v-application .msgUser {
  background-color: #fce0b8;
  text-align: right;
}
.v-card__title {
  display: block;
  font-size: 1.2rem;
  padding: 5px 10px;
}
.v-snack {
	margin-bottom: 400px;
}
.v-snack__content{
	color: black
}
</style>