<template>
  <div id="app">
    <section>
      <b-dropdown>
                 <button class="button is-primary" slot="trigger">
                     <span>Click me!</span>
                     <b-icon icon="menu-down"></b-icon>
                 </button>

                 <b-dropdown-item>Action</b-dropdown-item>
                 <b-dropdown-item>Another action</b-dropdown-item>
                 <b-dropdown-item>Something else</b-dropdown-item>
             </b-dropdown>
    </section>
    <!-- <img src="./assets/logo.png"> -->
  </div>
</template>

<script>
export default {
  name: 'app',
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
  }

  .header{
    background-color: red;
    padding: 0;
  }

  body{
    margin: 0
  }

  .el-row {
      margin-bottom: 20px;
      &:last-child {
        margin-bottom: 0;
      }
    }

</style>
