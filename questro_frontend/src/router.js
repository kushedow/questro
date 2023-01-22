import {createRouter, createWebHashHistory} from "vue-router";

import MainMenuPage from "@/components/MainMenuPage.vue";
import PickQuestionsPage from "@/components/PickQuestionsPage.vue";
import JoinPage from "@/components/JoinPage.vue";
import CreatePage from "@/components/CreatePage.vue";
import ResultsPage from "@/components/ResultsPage.vue";

import AnswerQuestionPage from "@/components/AnswerQuestionPage.vue";
import WaitForPickPage from "@/components/WaitForPickPage.vue";
import WaitForAnswerPage from "@/components/WaitForAnswerPage.vue";


import App from "@/App.vue";

export const router = new createRouter({
    history: createWebHashHistory(),
    routes: [

        // Страница меню
        { path: '/', component: MainMenuPage },

        // Создаем игру
        { path: '/create', component: CreatePage },
        // Присоединяемся к игре
        { path: '/join', component: JoinPage },
        // Показываем результаты
        { path: '/results', component: ResultsPage },

        // Выбрать страничку
        { path: '/pickquestion', component: PickQuestionsPage },
        // Ожидаем вопрос
        { path: '/waitforpick', component: WaitForPickPage },
        // Ожидаем ответ
        { path: '/waitforanswer', component: WaitForAnswerPage },
        // Отвечаем на вопрос
        { path: '/answerquestion', component: AnswerQuestionPage },

    ]
});