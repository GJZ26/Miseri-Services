/*=============================================
=               General Info DOM              =
=============================================*/

const light_level_sign = document.getElementById('light_level_sign');
const celsius_tem_sign = document.getElementById('celsius_tem_sign');
const fahrenheit_tem_sign = document.getElementById('fahrenheit_tem_sign');
const humidity_sign = document.getElementById('humidity_sign');

const air_quality_sign = document.getElementById('air_quality_sign');
const gas_presence_sign = document.getElementById('gas_presence_sign');

const air_quality_meter = document.getElementById('air_quality_meter');
const gas_presence_meter = document.getElementById('gas_presence_meter');

/*=============================================
=              Statistics Info DOM            =
=============================================*/

const gas_media = document.getElementById('gas_media');
const air_media = document.getElementById('air_media');
const tem_media = document.getElementById('tem_media');
const hum_media = document.getElementById('hum_media');
const light_media = document.getElementById('light_media');

const gas_range = document.getElementById('gas_range');
const air_range = document.getElementById('air_range');
const tem_range = document.getElementById('tem_range');
const hum_range = document.getElementById('hum_range');
const light_range = document.getElementById('light_range');

const gas_highest = document.getElementById('gas_highest');
const air_highest = document.getElementById('air_highest');
const tem_highest = document.getElementById('tem_highest');
const hum_highest = document.getElementById('hum_highest');
const light_highest = document.getElementById('light_highest');

const gas_lowest = document.getElementById('gas_lowest');
const air_lowest = document.getElementById('air_lowest');
const tem_lowest = document.getElementById('tem_lowest');
const hum_lowest = document.getElementById('hum_lowest');
const light_lowest = document.getElementById('light_lowest');

const gas_highest_time = document.getElementById('gas_highest_time');
const air_highest_time = document.getElementById('air_highest_time');
const tem_highest_time = document.getElementById('tem_highest_time');
const hum_highest_time = document.getElementById('hum_highest_time');
const light_highest_time = document.getElementById('light_highest_time');

const gas_lowest_time = document.getElementById('gas_lowest_time');
const air_lowest_time = document.getElementById('air_lowest_time');
const tem_lowest_time = document.getElementById('tem_lowest_time');
const hum_lowest_time = document.getElementById('hum_lowest_time');
const light_lowest_time = document.getElementById('light_lowest_time');

const gas_variation = document.getElementById('gas_variation');
const air_variation = document.getElementById('air_variation');
const tem_variation = document.getElementById('tem_variation');
const hum_variation = document.getElementById('hum_variation');
const light_variation = document.getElementById('light_variation');

/*=============================================
=                Log Console DOM             =
=============================================*/

const console_out = document.getElementById('console_log');

/*=============================================
=                App Info Modal              =
=============================================*/

/****************** Modals ********************/

const app_info_modal = document.getElementById('app_info_modal');
const preference_modal = document.getElementById('preference_modal');

/************** Modals Content *****************/

const client_version = document.getElementById('client_version');
const server_version = document.getElementById('server_version');
const rasp_version = document.getElementById('rasp_version');
const esp_version = document.getElementById('esp_version');

const light_sensor_mode = document.getElementsByName('light_sensor_mode');
const tem_sensor_mode = document.getElementsByName('tem_sensor_mode');
const hum_sensor_mode = document.getElementsByName('hum_sensor_mode');
const tem_mess = document.getElementsByName('tem_mess');
const data_calc = document.getElementsByName('data_calc');
const flick_screen = document.getElementsByName('flick_screen');
const sound_web = document.getElementsByName('sound_web');
const vibrate = document.getElementsByName('vibrate');
const led = document.getElementsByName('led');
const sound_device = document.getElementsByName('sound_device');
const autoscroll = document.getElementsByName('autoscroll');
const jsonformat = document.getElementsByName('jsonformat');

const gas_warn_inp = document.getElementById('gas_warn_inp');
const gas_alert_inp = document.getElementById('gas_alert_inp');
const air_warn_inp = document.getElementById('air_warn_inp');
const air_alert_inp = document.getElementById('air_alert_inp');

const sampling_time = document.getElementById('sampling_time');
const backup_time = document.getElementById('backup_time');

/*=============================================
=               Buttons DOM :)                =
=============================================*/

const clear_console_btn = document.getElementById('clear_console_btn');
const app_info_btn = document.getElementById('app_info_btn');
const preference_btn = document.getElementById('preference_btn');

const close_app_info_btn = document.getElementById('close_app_info_btn');
const close_preference_btn = document.getElementById('close_preference_btn');

/*=============================================
=           Local Events Handlers             =
=============================================*/

function showAppInfo() {
    app_info_modal.showModal()
}

function hiddenAppInfo() {
    app_info_modal.close()
}

function showPreferences() {
    preference_modal.showModal()
}

function hiddenPreferences() {
    preference_modal.close()
}

function clearConsole(){
    console_out.textContent=""
}


/*=============================================
=             Services Functions              =
=============================================*/





/*=============================================
=               EventListeners                =
=============================================*/

app_info_btn.onclick = showAppInfo
close_app_info_btn.onclick = hiddenAppInfo

preference_btn.onclick = showPreferences
close_preference_btn.onclick = hiddenPreferences

clear_console_btn.onclick = clearConsole


/*=============================================
=                   Websocket                 =
=============================================*/

import dataApp from "./manifest.json" assert {type: 'json'}

const socket = io(`${dataApp["websocket"]["protocol"]}://${dataApp["websocket"]["host"]}:${dataApp["websocket"]["port"]}/client`)