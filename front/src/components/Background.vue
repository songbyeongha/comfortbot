<template>
  <div id="wrapper">
    <div id="bg"></div>
    <div id="overlay"></div>
  </div>
</template>

<script>
export default {};
</script>

<style>
/* Wrapper */

@-moz-keyframes wrapper {
  0% {
    opacity: 0;
  }

  100% {
    opacity: 1;
  }
}

@-webkit-keyframes wrapper {
  0% {
    opacity: 0;
  }

  100% {
    opacity: 1;
  }
}

@-ms-keyframes wrapper {
  0% {
    opacity: 0;
  }

  100% {
    opacity: 1;
  }
}

@keyframes wrapper {
  0% {
    opacity: 0;
  }

  100% {
    opacity: 1;
  }
}

#wrapper {
  -moz-animation: wrapper 3s forwards;
  -webkit-animation: wrapper 3s forwards;
  -ms-animation: wrapper 3s forwards;
  animation: wrapper 3s forwards;
  height: 100%;
}

/* BG */

#bg {
  -moz-animation: bg 60s linear infinite;
  -webkit-animation: bg 60s linear infinite;
  -ms-animation: bg 60s linear infinite;
  animation: bg 60s linear infinite;
  -moz-backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  -ms-backface-visibility: hidden;
  backface-visibility: hidden;
  -moz-transform: translate3d(0, 0, 0);
  -webkit-transform: translate3d(0, 0, 0);
  -ms-transform: translate3d(0, 0, 0);
  transform: translate3d(0, 0, 0);

  background: #348cb2 url("../../public/img/background.jpg") bottom left;
  background-repeat: repeat-x;
  height: 100%;
  left: 0;
  opacity: 1;
  position: fixed;
  top: 0;
}

@-moz-keyframes bg {
  0% {
    -moz-transform: translate3d(0, 0, 0);
    -webkit-transform: translate3d(0, 0, 0);
    -ms-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
  }

  100% {
    -moz-transform: translate3d(-2250px, 0, 0);
    -webkit-transform: translate3d(-2250px, 0, 0);
    -ms-transform: translate3d(-2250px, 0, 0);
    transform: translate3d(-2250px, 0, 0);
  }
}

@-webkit-keyframes bg {
  0% {
    -moz-transform: translate3d(0, 0, 0);
    -webkit-transform: translate3d(0, 0, 0);
    -ms-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
  }

  100% {
    -moz-transform: translate3d(-2250px, 0, 0);
    -webkit-transform: translate3d(-2250px, 0, 0);
    -ms-transform: translate3d(-2250px, 0, 0);
    transform: translate3d(-2250px, 0, 0);
  }
}

@-ms-keyframes bg {
  0% {
    -moz-transform: translate3d(0, 0, 0);
    -webkit-transform: translate3d(0, 0, 0);
    -ms-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
  }

  100% {
    -moz-transform: translate3d(-2250px, 0, 0);
    -webkit-transform: translate3d(-2250px, 0, 0);
    -ms-transform: translate3d(-2250px, 0, 0);
    transform: translate3d(-2250px, 0, 0);
  }
}

@keyframes bg {
  0% {
    -moz-transform: translate3d(0, 0, 0);
    -webkit-transform: translate3d(0, 0, 0);
    -ms-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
  }

  100% {
    -moz-transform: translate3d(-2250px, 0, 0);
    -webkit-transform: translate3d(-2250px, 0, 0);
    -ms-transform: translate3d(-2250px, 0, 0);
    transform: translate3d(-2250px, 0, 0);
  }
}

#bg {
  background-size: 134vh auto;
  width: 6750px;
}

#overlay {
  background-attachment: fixed, fixed;
  background-image: url("../../public/img/overlay-pattern.png"),
    url("../../public/img/overlay.svg");
  background-position: top left, center center;
  background-repeat: repeat, no-repeat;
  background-size: auto, cover;
  height: 100%;
  left: 0;
  opacity: 1;
  position: fixed;
  top: 0;
  width: 100%;
}
</style>
