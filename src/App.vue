<template>
  <div id="app">
    <search-container>
      <div slot="form">
        <form>
        <div class="columns">
          <div class="column">
            <b-field label="Nombre">
              <b-input v-model="name"></b-input>
            </b-field>
          </div>
          <div class="column">
            <b-field label="Appellido">
              <b-input v-model="name"></b-input>
            </b-field>
          </div>
        </div>
        <div class="columns">
          <div class="column">
            <b-field label="Nombre">
              <b-input v-model="name"></b-input>
            </b-field>
          </div>
          <div class="column">
            <b-field label="Nombre">
              <b-input v-model="name"></b-input>
            </b-field>
          </div>
          <div class="column">
            <b-field label="Appellido">
              <b-input v-model="name"></b-input>
            </b-field>
          </div>
        </div>
        <div class="columns">
          <div class="column ">
            <input class="button is-primary" type="submit" @click.prevent="search" />             
          </div>
        </div>
        </form>
      </div>
    </search-container>
    <!-- <img src="./assets/logo.png"> -->
  </div>
</template>

<script>
import searchContainer from "./components/searchContainer.vue"

document.addEventListener('DOMContentLoaded', function () {

  // Get all "navbar-burger" elements
  var $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

  // Check if there are any navbar burgers
  if ($navbarBurgers.length > 0) {

    // Add a click event on each of them
    $navbarBurgers.forEach(function ($el) {
      $el.addEventListener('click', function () {

        // Get the target from the "data-target" attribute
        var target = $el.dataset.target;
        var $target = document.getElementById(target);

        // Toggle the class on both the "navbar-burger" and the "navbar-menu"
        $el.classList.toggle('is-active');
        $target.classList.toggle('is-active');

      });
    });
  }

});

export default {
  name: 'app',
  components: {
    searchContainer,
  },
  data () {
    return {
      currentDate: new Date(),
      num: 0,
      list: [
        {
          title: "Una carta",
          time: self.currentDate,
          btn: "Detalle"
        },
        {
          title: "Una carta de algo",
          time: self.currentDate,
          btn: "Detalle"
        },
        {
          title: "Entendimiento",
          time: self.currentDate,
          btn: "Detalle"
        },
        {
          title: "Algo de refexion",
          time: self.currentDate,
          btn: "Detalle"
        },
        {
          title: "Una carta",
          time: self.currentDate,
          btn: "Detalle"
        },
        {
          title: "Una carta",
          time: self.currentDate,
          btn: "Detalle"
        },
        {
          title: "Una carta",
          time: self.currentDate,
          btn: "Detalle"
        },

      ]
    }
  }
}
</script>

<style lang="scss">
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 10px;
  }

  .header{
    background-color: red;
    padding: 0;
  }

  .el-row {
      margin-bottom: 20px;
      &:last-child {
        margin-bottom: 0;
      }
    }

</style>
