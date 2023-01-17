import {createRouter, createWebHashHistory} from "vue-router";

import MainMenuPage from "@/components/MainMenuPage.vue";
import QuestionsPage from "@/components/QuestionsPage.vue";
import JoinPage from "@/components/JoinPage.vue";
import CreatePage from "@/components/CreatePage.vue";
import ResultsPage from "@/components/ResultsPage.vue";

import App from "@/App.vue";

export const router = new createRouter({
    history: createWebHashHistory(),
    routes: [
        { path: '/', component: MainMenuPage },
        { path: '/play', component: QuestionsPage },
        { path: '/join', component: JoinPage },
        { path: '/app', component: App },
        { path: '/create', component: CreatePage },
        { path: '/results', component: ResultsPage },
    ]
});