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

let localSettings = {
    "light_mode": 0, //          0 - A | 1 - B          | 2 - Both
    "tem_mode": 0, //            0 - A | 1 - B          | 2 - Both
    "hum_mode": 0, //            0 - A | 1 - B          | 2 - Both
    "tem_mes": 0, //       0 - Celsius | 1 - Fahrenheit | 2 - Both
    "screen_flick": 0, // 0 - Activate | 1 - Desactivate
    "play_sound": 0, //   0 - Activate | 1 - Desactivate
    "vibrate": 0, //      0 - Activate | 1 - Desactivate
    "autoscroll": 0, //   0 - Activate | 1 - Desactivate
    "formatJSON": 0 //    0 - Activate | 1 - Desactivate|
}

/*=============================================
=               Buttons DOM :)                =
=============================================*/

const clear_console_btn = document.getElementById('clear_console_btn');
const app_info_btn = document.getElementById('app_info_btn');
const preference_btn = document.getElementById('preference_btn');

const close_app_info_btn = document.getElementById('close_app_info_btn');
const close_preference_btn = document.getElementById('close_preference_btn');

/*=============================================
=              Events Handlers                =
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
    savePreferences()
    preference_modal.close()
}

function clearConsole() {
    console_out.textContent = ""
}

function updateGeneralView(data) {
    let temperature = 1
    let humidity = 1
    let light = 1

    if (localSettings["tem_mode"] === 0) temperature = data["hum_temp_a"]["temperature"]
    if (localSettings["tem_mode"] === 1) temperature = data["hum_temp_b"]["temperature"]
    if (localSettings["tem_mode"] === 2) temperature = (data["hum_temp_a"]["temperature"] + data["hum_temp_b"]["temperature"]) / 2

    if (localSettings["light_mode"] === 0) light = data["light_sensor_a"]["percent"]
    if (localSettings["light_mode"] === 1) light = data["light_sensor_b"]["percent"]
    if (localSettings["light_mode"] === 2) light = (data["light_sensor_a"]["percent"] + data["light_sensor_b"]["percent"]) / 2

    if (localSettings["hum_mode"] === 0) humidity = data["hum_temp_a"]["humidity"]
    if (localSettings["hum_mode"] === 1) humidity = data["hum_temp_b"]["humidity"]
    if (localSettings["hum_mode"] === 2) humidity = (data["hum_temp_a"]["humidity"] + data["hum_temp_b"]["humidity"]) / 2

    light_level_sign.textContent = `${light}%`

    celsius_tem_sign.textContent = localSettings["tem_mes"] === 1 ? `${(temperature * (9 / 5) + 32).toFixed(2)}°F` : `${(temperature).toFixed(2)}°C`

    fahrenheit_tem_sign.textContent = localSettings["tem_mes"] === 2 ? `/ ${(temperature * (9 / 5) + 32).toFixed(2)}°F` : ""

    humidity_sign.textContent = `${humidity}%`

    air_quality_sign.textContent = `${(data["air"]["co_ppm"]).toFixed(2)}ppm`
    air_quality_meter.value = data["air"]["co_ppm"]

    gas_presence_sign.textContent = `${(data["air"]["gas_ppm"]).toFixed(2)}ppm`
    gas_presence_meter.value = data["air"]["gas_ppm"]
}

/*=============================================
=             Services Functions              =
=============================================*/

function print(message) {
    console_out.innerHTML += '<b>></b> ' + message + '<br>'
}

function savePreferences() {
    light_sensor_mode.forEach((v, k) => { if (v.checked) localSettings["light_mode"] = k });
    tem_sensor_mode.forEach((v, k) => { if (v.checked) localSettings["tem_mode"] = k });
    hum_sensor_mode.forEach((v, k) => { if (v.checked) localSettings["hum_mode"] = k });
    tem_mess.forEach((v, k) => { if (v.checked) localSettings["tem_mes"] = k });
    flick_screen.forEach((v, k) => { if (v.checked) localSettings["screen_flick"] = k });
    sound_web.forEach((v, k) => { if (v.checked) localSettings["play_sound"] = k });
    vibrate.forEach((v, k) => { if (v.checked) localSettings["vibrate"] = k });
    autoscroll.forEach((v, k) => { if (v.checked) localSettings["autoscroll"] = k });
    jsonformat.forEach((v, k) => { if (v.checked) localSettings["formatJSON"] = k });
    localStorage.setItem('preferences', JSON.stringify(localSettings))
}

function loadLocalPreferences() {
    if (localStorage.getItem('preferences') !== null) localSettings = JSON.parse(localStorage.getItem('preferences'))

    light_sensor_mode[localSettings["light_mode"]].checked = true;
    tem_sensor_mode[localSettings["tem_mode"]].checked = true;
    hum_sensor_mode[localSettings["hum_mode"]].checked = true;
    tem_mess[localSettings["tem_mes"]].checked = true;
    flick_screen[localSettings["screen_flick"]].checked = true;
    sound_web[localSettings["play_sound"]].checked = true;
    vibrate[localSettings["vibrate"]].checked = true;
    autoscroll[localSettings["autoscroll"]].checked = true;
    jsonformat[localSettings["formatJSON"]].checked = true;
}

function webAlert(active) {
    if (active) {
        document.documentElement.classList.add("alert");
    }
    if (!active) {
        document.documentElement.classList.remove("alert")
    }
}

function loadStats(stats){
    gas_media.textContent = `${stats["gas_ppm"]["media"].toFixed(2)} ppm`
    gas_range.textContent = `${stats["gas_ppm"]["range"].toFixed(2)} ppm`
    gas_highest.textContent = `${stats["gas_ppm"]["highest"].toFixed(2)} ppm`
    gas_lowest.textContent = `${stats["gas_ppm"]["lowest"].toFixed(2)} ppm`
    gas_variation.textContent = stats["gas_ppm"]["varUnit"]

    air_media.textContent = `${stats["co_ppm"]["media"].toFixed(2)} ppm`
    air_range.textContent = `${stats["co_ppm"]["range"].toFixed(2)} ppm`
    air_highest.textContent = `${stats["co_ppm"]["highest"].toFixed(2)} ppm`
    air_lowest.textContent = `${stats["co_ppm"]["lowest"].toFixed(2)} ppm`
    air_variation.textContent = `${stats["co_ppm"]["varUnit"]}`

    hum_media.textContent = `${stats["hum"]["media"].toFixed(2)}%`
    hum_range.textContent = `${stats["hum"]["range"].toFixed(2)}%`
    hum_highest.textContent = `${stats["hum"]["highest"].toFixed(2)}%`
    hum_lowest.textContent = `${stats["hum"]["lowest"].toFixed(2)}%`
    hum_variation.textContent = `${stats["hum"]["varUnit"]}`

    light_media.textContent = `${stats["light"]["media"].toFixed(2)}%`
    light_range.textContent = `${stats["light"]["range"].toFixed(2)}%`
    light_highest.textContent = `${stats["light"]["highest"].toFixed(2)}%`
    light_lowest.textContent = `${stats["light"]["lowest"].toFixed(2)}%`
    light_variation.textContent = `${stats["light"]["varUnit"]}`

    tem_media.textContent = `${stats["tem"]["media"].toFixed(2)} °C`
    tem_range.textContent = `${stats["tem"]["range"].toFixed(2)} °C`
    tem_highest.textContent = `${stats["tem"]["highest"].toFixed(2)} °C`
    tem_lowest.textContent = `${stats["tem"]["lowest"].toFixed(2)} °C`
    tem_variation.textContent = `${stats["tem"]["varUnit"]}`
}

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

const protocol = dataApp["websocket"]["protocol"]
const host = dataApp["websocket"]["host"]
const port = dataApp["websocket"]["port"]
const namespace = dataApp["websocket"]["namespace"]

loadLocalPreferences()

const socket = io(`${protocol}://${host}:${port}/${namespace}`)

socket.on('log', (data) => {
    print(data)
})

socket.on('disconnect', () => {
    print("Connection with the server has been lost.")
})

socket.on('data', (data) => {
    updateGeneralView(data)
})

socket.on("stats", (data)=>{
    loadStats(data)
})