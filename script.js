function genChart() {
    ajaxGetRequest("/getData", displayBar);
    ajaxGetRequest("/getData", displayPie);
}

function getHourData() {
    let hour = document.getElementById("hour").value;
    ajaxPostRequest("/getDataCustom", JSON.stringify(hour), displayCustom);
}

function displayBar(resp) {
    let obj = {};
    let list = JSON.parse(resp);

    for (dict of list) {
        if (!(dict["year"] in obj)) {
            obj[dict["year"]] = 0;
        }
        obj[dict["year"]]++;
    }

    for (key in obj) {
        if (obj[key] < 20) {
            delete obj[key];
        }
    }

    let data = {
        x: Object.keys(obj),
        y: Object.values(obj),
        type: 'bar'
    };

    let layout = {
        title: 'Incidents by Date',
        xaxis: {title: 'Year'},
        yaxis: {title: '# of Incidents'},
    };
    
    Plotly.newPlot('div_bar', [data], layout);
}

function displayPie(resp) {

    let obj = {};
    let list = JSON.parse(resp);

    for (dict of list) {
        if (!(dict["day_of_week"] in obj)) {
            obj[dict["day_of_week"]] = 0;
        }
        obj[dict["day_of_week"]]++;
    }
    
    let data = [{
        values: Object.values(obj),
        labels: Object.keys(obj),
        type: 'pie'
    }];

    let layout = {
        "title": 'Incidents by Day of Week'
    };
    
    Plotly.newPlot('div_pie', data, layout);
}

function displayCustom(resp) {
    
    let obj = {};
    let list = JSON.parse(resp)["ls"];
    let hour = JSON.parse(resp)["hour"];
    
    for (dict of list) {
        if (dict["hour_of_day"] == hour) {
            if (!(dict["year"] in obj)) {
                obj[dict["year"]] = 0;
            }
            obj[dict["year"]]++;
        }
    }
    
    let data = [{
        x: Object.keys(obj),
        y: Object.values(obj),
        type: 'scatter'
    }];

    
    Plotly.newPlot('div_custom', data );
}

// Ajax
function ajaxGetRequest(path, callback){
    let request = new XMLHttpRequest();
    request.onreadystatechange = function(){
      if (this.readyState === 4 && this.status === 200){
          callback(this.response);
      }
    };
    request.open("GET", path);
    request.send();
  }
  
function ajaxPostRequest(path, data, callback) {
    let request = new XMLHttpRequest();
    request.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200){
            callback(this.response);
        }
    };
    request.open("POST", path);
    request.send(data);
}
