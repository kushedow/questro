# Стейты клиента

– loading (загружаемся, соединяемся с сокетом) >> menu

– menu (ничего не делаем, ждем ) >> create_game | join_game | rules

– create_game >> wait_to_join

– wait_to_join >> make_turn 

– join_game >> wait_turn

– rules >> menu

– make_turn >> wait_turn | finish

– wait_turn >> make_turn | finish

– finish >> menu | make_turn | wait_turn

– error | menu

# Стейты игры для сервера

– created

– turn

– finished


