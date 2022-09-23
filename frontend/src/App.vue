<template>
  <div id="wrapper">
    <nav class="navbar is-success is-large">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>KubSU</strong></router-link>

        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" >

          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>

        <div class="navbar-item has-dropdown is-hoverable">
          <a class="navbar-link" href="#">
            Факультеты
          </a>
          <div class="navbar-dropdown is-hidden-mobile is-boxed">
            <router-link to="/bf" class="navbar-item">Биологический факультет</router-link>

            <router-link to="/faid" class="navbar-item">Факультет архитектуры и дизайна</router-link>

            <router-link to="/fj" class="navbar-item">Факультет журналистики</router-link>

            <router-link to="/fisimo" class="navbar-item">Факультет истории, социологии и международных отношений
            </router-link>

            <router-link to="/fktpim" class="navbar-item">Факультет компьютерных технологий и прикладной математики
            </router-link>

            <router-link to="/fmikn" class="navbar-item">Факультет математики и компьютерных наук</router-link>

            <router-link to="/fppik" class="navbar-item">Факультет педагогики, психологии и коммуникативистики
            </router-link>

            <router-link to="/frgf" class="navbar-item">Факультет романо-германской филологии</router-link>

            <router-link to="/fuip" class="navbar-item">Факультет управления и психологии</router-link>

            <router-link to="/fhivt" class="navbar-item">Факультет химии и высоких технологий</router-link>

            <router-link to="/ftf" class="navbar-item">Физико-технический факультет</router-link>

            <router-link to="/ff" class="navbar-item">Филологический факультет</router-link>

            <router-link to="/hgh" class="navbar-item">Художественно-графический факультет</router-link>

            <router-link to="/ef" class="navbar-item">Экономический факультет</router-link>

            <router-link to="/uf" class="navbar-item">Юридический факультет</router-link>
          </div>
        </div>
      </div>
    </nav>

    <section class="section">
      <router-view/>
    </section>


    <footer class="footer">
      <div class="container">
        <div class="content has-text-centered">
          <a class="mx-2" href="https://vk.com"><img alt="vk" width="32" height="32"
                                                     src="https://upload.wikimedia.org/wikipedia/commons/2/21/VK.com-logo.svg"></a>
          <a class="mx-2" href="https://t.me/kubsunews"><img alt="telegram" width="32" height="32"
                                                             src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Telegram_2019_Logo.svg/1024px-Telegram_2019_Logo.svg.png"></a>
          <a class="mx-2" href="https://vk.com"><img alt="vk" width="32" height="32"
                                                     src="https://upload.wikimedia.org/wikipedia/commons/2/21/VK.com-logo.svg"></a>
          <a class="mx-2" href="https://t.me/kubsunews"><img alt="telegram" width="32" height="32"
                                                             src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Telegram_2019_Logo.svg/1024px-Telegram_2019_Logo.svg.png"></a>
          <p>© 2022 KubSU</p>
        </div>
      </div>
    </footer>
  </div>
</template>


<script>
export default {
  data() {
    return {
      showMobileMenu: false
      }
    }
}
</script>


<style lang="scss">
@import 'bulma';
</style>
