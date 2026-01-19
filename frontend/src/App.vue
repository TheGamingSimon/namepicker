<template>
  <nav>
    <router-link to="/">Namen ziehen</router-link>
    |
    <router-link to="/classes">Klassen verwalten</router-link>
  </nav>

  <router-view />
</template>

<style>
nav {
  padding: 1rem;
}
</style>
