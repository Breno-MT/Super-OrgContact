<template>

  <div class="container">        
      <img class="rounded float-start" src="@/assets/logo.jpg" alt="Login image">
      <div class="row justify-content-md-center">
          <div class="col-8 mt-5">
              <br>
              <h2 class="text-left">Bem-vindo(a) ao SuperOrg Project!</h2>
              <hr>
              <div class="row g-2">
                  <div class="col-15">
                      <button class="btn btn-success" @click="notWorking" >Google</button>
                  </div>

              </div>
          </div>
      </div>
  </div>


</template>
  

<script>

</script>

<style scoped>
  body {
    background-color: rgb(66, 79, 82);
    text-align: center;
  }
  h1 {
    font-size: 2vh;
  }
  img {
    width: 520px;
    height: 420px;
  }
</style>