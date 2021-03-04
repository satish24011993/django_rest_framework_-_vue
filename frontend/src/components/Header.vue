<template>
    <div class="app">
        <b-navbar toggleable="lg" type="dark" variant="info">
            <b-navbar-brand class="text-white" href="#">Youtube Rater</b-navbar-brand>
            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

            <b-navbar-nav class="ml-auto">
                <b-nav-form @submit.prevent="login">
                    <b-form-input id="username" size="sm" class="mr-sm-2" v-model="username" placeholder="username" name="username"></b-form-input>
                    <b-form-input id="password" size="sm" class="mr-sm-2" placeholder="password" type="password" v-model="password" name="password"></b-form-input>

                    <b-button size="sm" class="my-2 my-sm-0" type="submit">Login</b-button>
                
                </b-nav-form>

                <!-- </b-nav-form> -->

                <!-- </b-nav-form>

                </b-nav-form> -->


                </b-navbar-nav>
            <!-- </b-collapse> -->
        </b-navbar>
    </div>
</template>

<script>

import axios from 'axios'

export default {
    name: 'Header',
    components: {

    },
    data() {
        return {
            username: '',
            password: ''
            }
        },
    methods: {
        login() {
            axios.post('http://127.0.0.1:8000/auth/', {
                username: this.username,
                password: this.password,
            })
            .then(resp => console.log(resp))
            .catch(err => console.log(err))
        }
    }
}
</script>