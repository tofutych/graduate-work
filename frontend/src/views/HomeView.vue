<template>
  <div class="home">
    <section class="hero is-info">
      <div class="hero-body has-text-centered">
        <p class="title">
          Кубанский государственный университет
        </p>
      </div>

      <div class="columns is-multiline is-centered">
        <div class="column is-12">
          <h2 class="is-size-2 has-text-centered">Факультеты</h2>
        </div>

        <div class="column is-7 py-3"
             v-for="faculty in faculties"
             v-bind:key="faculty.id"
        >
          <div class="box has-text-centered">
            <h3 class="is-size-4">{{ faculty.name }}</h3>
          </div>

        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HomeView',

  data() {
    return {
      faculties: []
    }
  },

  components: {},

  mounted() {
    this.getFaculties()
  },

  methods: {
    getFaculties() {
      axios
          .get('/api/v1/faculties/')
          .then(response => {
            this.faculties = response.data
          })
          .catch(error => {
            console.log(error)
          })
    }
  }
}
</script>
