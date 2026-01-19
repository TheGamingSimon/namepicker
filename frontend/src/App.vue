<template>
  <img src="./assets/classroom.jpg" alt="classroom  " />
  <nav>
    <router-link to="/">Namen ziehen</router-link>
    |
    <router-link to="/classes">Klassen verwalten</router-link>
  </nav>

  <router-view />
</template>

<style>
h2 {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  font-weight: normal;
  color: #2c3e50;
  margin-bottom: 1rem;
}
nav {
  text-align: left;
  margin: 1rem 0;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
}
nav a {
  text-decoration: none;
  color: #42b983;
}
nav a.router-link-exact-active {
  font-weight: bold;
  color: #35495e;
}
img {
  width: 100%;
  max-height: 300px;
  object-fit: cover;
  margin-bottom: 1rem;
}
</style>
