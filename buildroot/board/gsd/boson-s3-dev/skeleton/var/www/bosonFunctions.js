var xmlhttp;
xmlhttp = new XMLHttpRequest();

function setColor(button_id) {
    colorxhr = new XMLHttpRequest();
    var data = new FormData();

    data.append("color_palette", button_id)

    colorxhr.open("POST", "cgi-bin/setColor_palette.py", true);
    colorxhr.send(data);
}

function setFfcMode() {
    var ffcmodexhr = new XMLHttpRequest();
    ffcmodexhr.responseType = 'json'

    ffcmodexhr.onreadystatechange = function() {
        if (ffcmodexhr.readyState == 4 && ffcmodexhr.status == 200) {
            getFfcState();
        }
    };

    var data = new FormData();
    var modeSetting = document.getElementById("ffc_mode");

    data.append("ffc_mode", modeSetting.value)

    ffcmodexhr.open("POST", "cgi-bin/setFfc_mode.py", true);
    ffcmodexhr.send(data);
}

function setFfcGain() {
    var ffcgainxhr = new XMLHttpRequest();
    ffcgainxhr.responseType = 'json'

    ffcgainxhr.onreadystatechange = function() {
        if (ffcgainxhr.readyState == 4 && ffcgainxhr.status == 200) {
            getFfcState();
        }
    };

    var data = new FormData();
    var modeSetting = document.getElementById("ffc_gain");

    data.append("ffc_gain", modeSetting.value)

    ffcgainxhr.open("POST", "cgi-bin/setFfc_gain.py", true);
    ffcgainxhr.send(data);
}

function setFfcInt() {
    var ffcintxhr = new XMLHttpRequest();
    ffcintxhr.responseType = 'json'

    ffcintxhr.onreadystatechange = function() {
        if (ffcintxhr.readyState == 4 && ffcintxhr.status == 200) {
            getFfcState();
        }
    };

    var data = new FormData();
    var modeSetting = document.getElementById("ffc_int");

    data.append("ffc_int", modeSetting.value)

    ffcintxhr.open("POST", "cgi-bin/setFfc_int.py", true);
    ffcintxhr.send(data);
}

function runFfc() {
    xmlhttp.open("GET", "cgi-bin/runFfc.py", true);
    xmlhttp.send();
}

function getZoomState() {
    var curZxhr = new XMLHttpRequest();
    curZxhr.responseType = 'json'

    curZxhr.onreadystatechange = function() {
        if (curZxhr.readyState == 4 && curZxhr.status == 200) {
            let responseObj = curZxhr.response;
            document.getElementById("xloc").value = responseObj.x_location;
            document.getElementById("yloc").value = responseObj.y_location;
            document.getElementById("zoom").value = responseObj.zoom;
        }
     };

     curZxhr.open("GET", "cgi-bin/getZoom_state.py", true);
     curZxhr.send();
}

function setZoomState() {
    var zoomxhr = new XMLHttpRequest();

    zoomxhr.onreadystatechange = function() {
        if (zoomxhr.readyState == 4 && zoomxhr.status == 200) {
            getZoomState();
        }
     };

    var data = new FormData();
    var x = document.getElementById("zoom_x");
    var y = document.getElementById("zoom_y");
    var z = document.getElementById("zoom_level");

    data.append("zoom_x", x.value)
    data.append("zoom_y", y.value)
    data.append("zoom_level", z.value)

    zoomxhr.open("POST", "cgi-bin/setZoom_state.py", true);
    zoomxhr.send(data);
}

function setFfcPeriod() {
    var ffcperiodxhr = new XMLHttpRequest();
    ffcperiodxhr.responseType = 'json'

    ffcperiodxhr.onreadystatechange = function() {
        if (ffcperiodxhr.readyState == 4 && ffcperiodxhr.status == 200) {
            getFfcState();
        }
    };

    var data = new FormData();
    var period = document.getElementById("ffc_frame");

    data.append("ffc_frame", period.value);

    ffcperiodxhr.open("POST", "cgi-bin/setFfcFrames_threshold.py", true);
    ffcperiodxhr.send(data);
}

function setFfcTempDelta() {
    var ffctempdxhr = new XMLHttpRequest();
    ffctempdxhr.responseType = 'json'

    ffctempdxhr.onreadystatechange = function() {
        if (ffctempdxhr.readyState == 4 && ffctempdxhr.status == 200) {
            getFfcState();
        }
    };

    var data = new FormData();
    var temp = document.getElementById("ffc_temp");

    data.append("ffc_temp", temp.value);

    ffctempdxhr.open("POST", "cgi-bin/setFfcTemp_delta.py", true);
    ffctempdxhr.send(data);
}

function getCameraInfo() {
    var infoxhr = new XMLHttpRequest();
    infoxhr.responseType = 'json';

    infoxhr.onreadystatechange = function() {
        if (infoxhr.readyState == 4 && infoxhr.status == 200) {
            let responseObj = infoxhr.response;
            document.getElementById("camera_pn").value = responseObj.camera_pn;
            document.getElementById("camera_sn").value = responseObj.camera_sn;
            document.getElementById("sensor_sn").value = responseObj.sensor_sn;
            document.getElementById("software_rev").value = responseObj.software_rev;
        }
     };

     infoxhr.open("GET", "cgi-bin/getCamera_info.py", true);
     infoxhr.send();
}

function getFfcState() {
    var ffcxhr = new XMLHttpRequest();
    ffcxhr.responseType = 'json';

    ffcxhr.onreadystatechange = function() {
        if (ffcxhr.readyState == 4 && ffcxhr.status == 200) {
            let responseObj = ffcxhr.response;
            document.getElementById("ffc_frames").value = responseObj.ffc_frames;
            document.getElementById("ffc_period").value = responseObj.ffc_period;
            document.getElementById("ffc_delta").value = responseObj.ffc_delta;
            document.getElementById("ffc_ltemp").value = responseObj.ffc_ltemp;
            document.getElementById("fpa_temp").value = responseObj.fpa_temp;
            document.getElementById("ffc_modes").value = responseObj.ffc_mode;
            document.getElementById("ffc_gains").value = responseObj.ffc_gain;
        }
     };

     ffcxhr.open("GET", "cgi-bin/getFfc_settings.py", true);
     ffcxhr.send();
}

function setRoi(button_id) {
    var setroixhr = new XMLHttpRequest();
    setroixhr.responseType = 'json'

    setroixhr.onreadystatechange = function() {
        if (setroixhr.readyState == 4 && setroixhr.status == 200) {
            getRoiStatistics();
        }
    };
    var data = new FormData();

    if (button_id == "setroi") {
        var x_center = document.getElementById("pos_x");
        var y_center = document.getElementById("pos_y");
        var width = document.getElementById("roi_width");
        var height = document.getElementById("roi_height");
    
        document.getElementById("slide_x").value = x_center.value;
        document.getElementById("slide_y").value = y_center.value;
    
        data.append("pos_x", x_center.value);
        data.append("pos_y", y_center.value);
        data.append("roi_width", width.value);
        data.append("roi_height", height.value);
        data.append("show_region", "true");
    }
    else {
        data.append("pos_x", "320");
        data.append("pos_y", "256");
        data.append("roi_width", "640");
        data.append("roi_height", "512");
        data.append("show_region", "false");
    }


    setroixhr.open("POST", "cgi-bin/setRoi_region.py", true);
    setroixhr.send(data);
}

function setSpotEnable(button_id) {
    var spotenablexhr = new XMLHttpRequest();
    var data = new FormData();
    spotenablexhr.responseType = 'json'

    var units = document.querySelector('input[name="temp_units"]:checked').value

    if (button_id == "spotEnable") {
        data.append("enable", "true")
        data.append("units", units)
    }
    if (button_id == "spotDisable") {
        data.append("enable", "false")
    }

    spotenablexhr.open("POST", "cgi-bin/setSpot_enable.py", true);
    spotenablexhr.send(data);
}

function setSpotRoi(button_id) {
    var setspotroixhr = new XMLHttpRequest();
    setspotroixhr.responseType = 'json'

    setspotroixhr.onreadystatechange = function() {
        if (setspotroixhr.readyState == 4 && setspotroixhr.status == 200) {
            getRoiStatistics();
        }
    };
    var data = new FormData();

    if (button_id == "set_spot_roi") {
        var x_center = document.getElementById("spot_x");
        var y_center = document.getElementById("spot_y");
        var width = document.getElementById("spot_width");
        var height = document.getElementById("spot_height");
    
        data.append("pos_x", x_center.value);
        data.append("pos_y", y_center.value);
        data.append("roi_width", width.value);
        data.append("roi_height", height.value);
        data.append("show_region", "true");
    }
    else {
        data.append("pos_x", "320");
        data.append("pos_y", "256");
        data.append("roi_width", "640");
        data.append("roi_height", "512");
        data.append("show_region", "false");
    }


    setspotroixhr.open("POST", "cgi-bin/setSpot_roi.py", true);
    setspotroixhr.send(data);
}

function getSpotStatistics() {
    var spotroixhr = new XMLHttpRequest();
    spotroixhr.responseType = 'json';

        spotroixhr.onreadystatechange = function() {
        if (spotroixhr.readyState == 4 && spotroixhr.status == 200) {
            let responseObj = spotroixhr.response;

            document.getElementById("spot_center_x").value = responseObj.center_x;
            document.getElementById("spot_center_y").value = responseObj.center_y;
            document.getElementById("spot_roi_h").value = responseObj.roi_h;
            document.getElementById("spot_roi_w").value = responseObj.roi_w;

            document.getElementById("spot_x").value = responseObj.center_x;
            document.getElementById("spot_y").value = responseObj.center_y;
            document.getElementById("spot_width").value = responseObj.roi_w;
            document.getElementById("spot_height").value = responseObj.roi_h;

            document.getElementById("spot_min_value").value = responseObj.min_spot;
            document.getElementById("spot_max_value").value = responseObj.max_spot;
            document.getElementById("spot_avg_value").value = responseObj.mean_val;

            document.getElementById("temp_min_value").value = responseObj.min_temp;
            document.getElementById("temp_max_value").value = responseObj.max_temp;
            document.getElementById("temp_avg_value").value = responseObj.mean_temp;

        }
     };

     spotroixhr.open("GET", "cgi-bin/getSpot_statistics.py", true);
     spotroixhr.send();
}

function getRoiStatistics() {
    var roixhr = new XMLHttpRequest();
    roixhr.responseType = 'json';

    roixhr.onreadystatechange = function() {
        if (roixhr.readyState == 4 && roixhr.status == 200) {
            let responseObj = roixhr.response;

            document.getElementById("center_x").value = responseObj.center_x;
            document.getElementById("center_y").value = responseObj.center_y;
            document.getElementById("roi_h").value = responseObj.roi_h;
            document.getElementById("roi_w").value = responseObj.roi_w;
            document.getElementById("min_value").value = responseObj.min_value;
            document.getElementById("max_value").value = responseObj.max_value;
            document.getElementById("avg_value").value = responseObj.avg_value;
            document.getElementById("pos_x").value = responseObj.center_x;
            document.getElementById("pos_y").value = responseObj.center_y;
            document.getElementById("roi_width").value = responseObj.roi_w;
            document.getElementById("roi_height").value = responseObj.roi_h;
        }
     };

     roixhr.open("GET", "cgi-bin/getRoi_statistics.py", true);
     roixhr.send();
}

function setRoi_x() {
    var data = new FormData();
    var x_center = document.getElementById("slide_x");
    var y_center = document.getElementById("pos_y");
    var width = document.getElementById("roi_width");
    var height = document.getElementById("roi_height");

    document.getElementById("pos_x").value = x_center.value;

    data.append("pos_x", x_center.value);
    data.append("pos_y", y_center.value);
    data.append("roi_width", width.value);
    data.append("roi_height", height.value);

    xmlhttp.open("POST", "cgi-bin/setRoi_region.py", true);
    xmlhttp.send(data);
}

function setRoi_y() {
    var data = new FormData();
    var x_center = document.getElementById("pos_x");
    var y_center = document.getElementById("slide_y");
    var width = document.getElementById("roi_width");
    var height = document.getElementById("roi_height");

    document.getElementById("pos_y").value = y_center.value;

    data.append("pos_x", x_center.value);
    data.append("pos_y", y_center.value);
    data.append("roi_width", width.value);
    data.append("roi_height", height.value);

    xmlhttp.open("POST", "cgi-bin/setRoi_region.py", true);
    xmlhttp.send(data);
}

function setPassword() {
    var data = new FormData();
    var setxhr = new XMLHttpRequest();
    setxhr.responseType = 'json'

    var new_user = document.getElementById("new_user");
    var new_pwd = document.getElementById("new_pwd");

    data.append("action", "set");
    data.append("new_user", new_user.value);
    data.append("new_pwd", new_pwd.value);

    setxhr.open("POST", "cgi-bin/system_settings.py", true);
    setxhr.send(data);
}

function getPassword() {
    var data = new FormData();
    var pwdxhr = new XMLHttpRequest();
    pwdxhr.responseType = 'json'

    pwdxhr.onreadystatechange = function() {
        if (pwdxhr.readyState == 4 && pwdxhr.status == 200) {
            let responseObj = pwdxhr.response;
            document.getElementById("cur_user").value = responseObj.cur_user;
            document.getElementById("cur_pwd").value = responseObj.cur_pwd;
        }
    };

    data.append("action", "get");

    pwdxhr.open("POST", "cgi-bin/system_settings.py", true);
    pwdxhr.send(data);
}

function resetWebServer() {
    var data = new FormData();
    var serverxhr = new XMLHttpRequest();
    serverxhr.responseType = 'json'

    serverxhr.onreadystatechange = function() {
        if (serverxhr.readyState == 4 && serverxhr.status == 200) {
            window.alert("Webserver has been Reset. Please refresh webpage.")
        }
    };

    data.append("action", "resetServer");

    serverxhr.open("POST", "cgi-bin/system_settings.py", true);
    serverxhr.send(data);
}

function resetCamera() {
    var data = new FormData();
    var setxhr = new XMLHttpRequest();
    setxhr.responseType = 'json'

    setxhr.onreadystatechange = function() {
        if (setxhr.readyState == 4 && setxhr.status == 200) {
            
        }
    };

    data.append("action", "resetCamera");

    setxhr.open("POST", "cgi-bin/system_settings.py", true);
    setxhr.send(data);
}

function resetSystem() {
    var data = new FormData();
    var setxhr = new XMLHttpRequest();
    setxhr.responseType = 'json'

    setxhr.onreadystatechange = function() {
        if (setxhr.readyState == 4 && setxhr.status == 200) {
            
        }
    };

    data.append("action", "resetSystem");

    setxhr.open("POST", "cgi-bin/system_settings.py", true);
    setxhr.send(data);
}

function resetRtspStream() {
    var data = new FormData();
    var setxhr = new XMLHttpRequest();
    setxhr.responseType = 'json'

    setxhr.onreadystatechange = function() {
        if (setxhr.readyState == 4 && setxhr.status == 200) {
            
        }
    };

    data.append("action", "resetStream");

    setxhr.open("POST", "cgi-bin/system_settings.py", true);
    setxhr.send(data);
}