Number.prototype.formatAsString = function(c, d, t){
    var n = this, c = isNaN(c = Math.abs(c)) ? 2 : c, d = d == undefined ? "," : d, t = t == undefined ? "." : t, s = n < 0 ? "-" : "", i = parseInt(n = Math.abs(+n || 0).toFixed(c)) + "", j = (j = i.length) > 3 ? j % 3 : 0;
    return s + (j ? i.substr(0, j) + t : "") + i.substr(j).replace(/(\d{3})(?=\d)/g, "$1" + t) + (c ? d + Math.abs(n - i).toFixed(c).slice(2) : "");
};

var regionGroups = {
    1:[],
    2:[3,4,5,6,7,8,9,10,11,12,13,14],
    15:[16,17,18,19,20,21,22,23,24,25],
    26:[27,28,29,30,31,32,33,34,35,36,37,38,39],
    40:[41,42,43,44,45,46,47,48],
    49:[50,51,52,53,54,55],
    56:[57,58,59],
    60:[]
};

var defaultInputs;

var sliderParams = {
    "pResilience" : {
        'id': 'resilience',
        'inputName': 'inputResilienceYears',
        'displayRatio': 1,
        'caption': 'TIME FRAME',
        'desc': 'Continuous years',
        'min':1, 
        'max':150,
        'unit':'&nbsp;yr',
        'rules': [[1,""],[50,""],[100,""],[150,""]]
    },
    "pFoodRatio" : {
        'id': 'food',
        'inputName': 'inputFoodRatio',
        'displayRatio': 100,
        'caption': 'TOTAL FOOD',
        'desc': '% of food to be produced',
        'min':0, 
        'max':500,
        'unit':'%',
        'rules': [[0,""],[100,""],[200,""],[300,""],[400,""],[500,""]]
    },
    "pMeateggRatio" : {
        'id': 'meategg',
        'inputName': 'inputMeateggRatio',
        'displayRatio': 100,
        'caption': 'MEAT - EGGS',
        'desc': '% of diet',
        'min':0, 
        'max':15,
        'unit':'%',
        'step':0.5,
        'rules': [[0,"Vegan"],[1.5,"Vegetarian (inc.eggs)"],[2.5,"Vegetarian (inc. eggs & diary)"],[7.5,"Healthy level"],[13,"2011 level"],[15,""]]
    },
    "pRedmeatRatio" : {
        'id': 'redmeat',
        'inputName': 'inputRedmeatRatio',
        'displayRatio': 100,
        'caption': 'RED MEAT',
        'desc': '% of all meat (if meat diet)',
        'unit':'%',
        'rules': [[0,"100% white meat"],[50,""],[64,"2011 level"],[100,"0% white meat"]]
    },
    "pActivityLevel" : {
        'id': 'activity',
        'inputName': 'inputActivityLevel',
        'displayRatio': 1,
        'caption': 'ACTIVITY LEVEL',
        'desc': 'Average for population',
        'min':1, 
        'max':3,
        'rules': [[1,"Sedentary"],[2,"Moderate"],[3,"High"]]
    },
    "pLossesRatio" : {
        'id': 'losses',
        'inputName': 'inputLossesRatio',
        'displayRatio': 100,
        'caption': 'AVOIDABLE WASTE',
        'desc': '% of all food produced',
        'min':0, 
        'max':20,
        'unit':'%',
        'rules': [[0,""],[10,""],[12,"2011 level"],[20,""]]
    },
    "pRecyclingRatio" : {
        'id': 'recycling',
        'inputName': 'inputRecyclingRatio',
        'displayRatio': 100,
        'caption': 'RECYCLING',
        'desc': '% of food wastage fed to farm animals',
        'unit':'%',
        'rules': [[0,"2011 level"],[50,""],[100,""]]
    },
    "pOrganicRatio" : {
        'id': 'organic',
        'inputName': 'inputOrganicRatio',
        'displayRatio': 100,
        'caption': 'ORGANIC FARMING',
        'desc': '% of all agricultural land',
        'unit':'%',
        'rules': [[0,"100% conventional"],[50,""],[100,"0% conventional"]]
    },
    "pIrrigationRatio" : {
        'id': 'irrigation',
        'inputName': 'inputIrrigationRatio',
        'displayRatio': 100,
        'caption': 'IRRIGATION',
        'desc': '% of all irrigated land',
        'unit':'%',
        'rules': [[0,""],[50,""],[100,""]]
    },
    "pFuelTotal" : {
        'id': 'fuel',
        'inputName': 'inputFuelTotal',
        'displayRatio': 1,
        'caption': 'ALL LIQUID FUEL',
        'desc': 'Liquid fuel litres/p/year',
        'min':0, 
        'max':3000,
        'unit':'&nbsp;lt',
        'rules': [[0,""],[1000,""],[2000,""],[2600,"2011 level"],[3000,""]]
    },
    "pBiofuelRatio" : {
        'id': 'biofuel',
        'inputName': 'inputBiofuelRatio',
        'displayRatio': 100,
        'caption': 'BIOFUEL',
        'desc': '% of all liquid fuel',
        'unit':'%',
        'rules': [[0,""],[50,""],[100,""]]
    },
    "pFibreTotal" : {
        'id': 'fibre',
        'inputName': 'inputFibreTotal',
        'displayRatio': 1,
        'caption': 'ALL TEXTILES',
        'desc': 'kg/p/year',
        'min':0, 
        'max':30,
        'unit':'&nbsp;kg',
        'rules': [[0,""],[10,""],[23,"2011 level"],[30,""]]
    },
    "pFibreNaturalRatio" : {
        'id': 'fibreNat',
        'inputName': 'inputFibreNaturalRatio',
        'displayRatio': 100,
        'caption': 'NATURAL FIBRE',
        'desc': '% of all natural fibre',
        'unit':'%',
        'rules': [[0,"100% synthetic"],[50,"2011 level"],[100,"0% synthetic"]]
    },
    "pFibreWoolRatio" : {
        'id': 'fibreWool',
        'inputName': 'inputFibreWoolRatio',
        'displayRatio': 100,
        'caption': 'WOOL FIBRE',
        'desc': '% of all wool fibre',
        'unit':'%',
        'rules': [[0,"100% cotton"],[12,"2011 level"],[50,""],[100,"0% cotton"]]
    },
    "pTimber" : {
        'id': 'timber',
        'inputName': 'inputTimber',
        'displayRatio': 1,
        'caption': '&#160;',
        'desc': 'All uses - m<sup>3</sup>/p/year',
        'min':0, 
        'max':10,
        'unit':'&nbsp;m<sup>3</sup>',
        'step':0.1,
        'rules': [[0,""],[5,""],[10,""]]
    },
    "pInfrastructure" : {
        'id': 'infrastr2',
        'inputName': 'inputInfrastructure',
        'displayRatio': 1,
        'caption': '&#160;',
        'desc': 'Buildings, roads, etc - m<sup>2</sup>/p',
        'min':0, 
        'max':2000,
        'unit':'&nbsp;m<sup>2</sup>',
        'rules': [[0,""],[730,"2011 level (excluding private green space)"],[1000,""],[1600,"2011 level (including private green space)"],[2000,""]]
    },
    "pNatureRatio" : {
        'id': 'nature2',
        'inputName': 'inputNatureRatio',
        'displayRatio': 100,
        'caption': '&#160;',
        'desc': '% of all land',
        'unit':'%',
        'rules': [[0,""],[23,"2011 level"],[50,""],[100,""]]
    }
};
  
//jQuery plugin to create an extended slider
(function( $ ) {
    $.fn.sliderPanel = function( options ) {
        if ( options=="value" ) {
            var param = Array.prototype.slice.call( arguments, 1 );
            if (param.length==0) {
                return this.data('textbox').val();
            } else if (param.length==1) {
                return this.each(function() {
                    $(this).data('textbox').val(param[0]);
                    $(this).data('slider').slider("value",param[0]);
                });
            } else if (param.length>1) {
                for (var i=0; i<param.length; ++i) {
                    if (!this.get(i)) break;
                    $(this.get(i)).data('textbox').val(param[0]);
                    $(this.get(i)).data('slider').slider("value",param[0]);
                }
            }
            return this;
        } else {
      
            var opt = $.extend( {
                'caption':'',
                'desc':'',
                'unit':'',
                'orientation': "vertical",
                'min' : 0,
                'max' : 100,
                'value' : 0
            }, options);
    
            return this.each(function() {
                var $this = $(this);
                $this.empty();
                //$this.attr("title",opt.desc);
                var label = $('<label></label>').html('<a class="label-caption help-link" href="#">'+opt.caption+'</a>').appendTo($this);
                var textbox = $('<input type="text" '+'name="'+opt.inputName+'" />').appendTo(label); //id="'+opt.id
                if (opt.unit) label.append(" " + opt.unit);
                opt = $.extend( {
                    'slide' : function( event, ui ) {
                        textbox.val( ui.value );
                    },
                    'stop' : function( event, ui ) {
                        $this.change();
                    }
                }, opt);
                var sliderContainer = $('<div class="ui-slider-container ui-widget"></div>');
                sliderContainer.appendTo($this);
                //create slider
                var sliderBlock = $('<div></div>').slider(opt).appendTo(sliderContainer);
                // create slider rules
                if (opt.rules) {
                    var sliderDecor = $('<div class="ui-slider-decoration-v"></div>').appendTo(sliderContainer);
                    if (!sliderDecor.height()) sliderDecor.height(sliderBlock.height());
                    var rulesMarks = $('<div class="ui-slider-rules-v"></div>').appendTo(sliderDecor);
                    var rulesLabels = $('<div class="ui-slider-rules-labels ui-slider-rules-labels-v">').appendTo(sliderDecor);
                    var maxwidth=0;
                    for (var i=0; i<opt.rules.length; ++i) {
                        var v = opt.rules[i][0];
                        var pos = 100 - ( (v-opt.min)*100/(opt.max-opt.min) );
                        var labeltext = '' + v + opt.unit;
                        $('<div class="ui-slider-rules-mark-v"></div>').css("top",pos+"%").appendTo(rulesMarks);
                        var l = $('<div class="ui-slider-rules-label-v">'+labeltext+'</div>').css("top",pos+"%").appendTo(rulesLabels);
                        if (l.width() > maxwidth) maxwidth = l.width();
                    }
                    rulesLabels.width(maxwidth);
                }
                textbox.on("change focusout keypress", function(event){
                    if (event.type == "keypress" && event.which != 13) return;
                    var v = $(this).val();
                    if (isNumber(v) && (v >= opt.min && v <= opt.max)) {
                        sliderBlock.slider("value",v);
                    } else {
                        $(this).val(sliderBlock.slider("value"));
                        $(this).focus();
                        var paramtitle = $(this).siblings('.label-caption').text();
                        alert(paramtitle+": Please enter a value between "+opt.min+" and "+opt.max+".");
                    }
                });
                $this.data('textbox',textbox);
                $this.data('slider',sliderBlock);
            });//each
    
        }//if
    };//$.fn.sliderPanel

})( jQuery );

function isNumber(n) {
    return !isNaN(parseFloat(n)) && isFinite(n);
}

function CsvToObjects(data) {
    var objects = new Array;
    var rows = data.split(/\r\n|\n/);
    var fieldNames = rows[0].split(',');
    for (var i=1; i<rows.length; ++i) {
        var cells = rows[i].split(',');
        var obj = new Object;
        for (var j=0; j<cells.length; ++j) {
            if (isNumber(cells[j])) {
                obj[fieldNames[j]] = Number(cells[j]);
            } else {
                obj[fieldNames[j]] = cells[j];
            }
        }
        objects.push(obj);
    }
    return objects;
}

function updateInputValues(regionId) {
    var i=regionId;
    var di = defaultInputs[i];
    $('#inputRegionId').val(regionId);
    $('#inputPopulation').val(di.population.formatAsString(0,'.',','));
    $('#inputAreasCropping').val(di.cropping.formatAsString(0,'.',','));
    $('#inputAreasPasture').val(di.pasture.formatAsString(0,'.',','));
    $('#inputAreasNonAg').val(di.nonAg.formatAsString(0,'.',','));
    $('#inputAreasBuilt').val(di.infrastr1.formatAsString(0,'.',','));
    $('#inputAreasNature').val(di.nature1.formatAsString(0,'.',','));
    var totalArea = di.cropping + di.pasture + di.nonAg + di.infrastr1 + di.nature1;
    $('#inputAreasTotal').val(totalArea.formatAsString(0,'.',',')).attr('readonly', true);

    for (var key in sliderParams) {
        var p = sliderParams[key];
        var v = di[p.id] * p.displayRatio;
        if (v % 1 != 0) v = v.toFixed(1);
        p.panel.sliderPanel("value", v);
    }
}

function updateInputAreasTotal() {
    var cropping = parseInt($('#inputAreasCropping').val().replace(/[\D]/g, ""));
    var pasture = parseInt($('#inputAreasPasture').val().replace(/[\D]/g, ""));
    var nonag = parseInt($('#inputAreasNonAg').val().replace(/[\D]/g, ""));
    var built = parseInt($('#inputAreasBuilt').val().replace(/[\D]/g, ""));
    var nature = parseInt($('#inputAreasNature').val().replace(/[\D]/g, ""));      
    var totalArea = cropping + pasture + nonag + built + nature;
    $('#inputAreasTotal').val(totalArea.formatAsString(0,'.',','));
}

function updatePopulation() {
    var population = parseInt($('#inputPopulation').val().replace(/[\D]/g, ""));
    var projectedPopulation = parseInt($('#outputPopcc').text().replace(/[\D]/g, ""));
    var v1 = $("#outputCapacityText"); 
    var v2 = $("#outputCapacityPercentage");
    if(projectedPopulation > 0){
        var p = population / projectedPopulation * 100;
        v2.text(parseFloat(p).toFixed(1)+"%");  
    } else {
        v2.text("&infin;%"); 
        //v2.css("font-size","1.4em");  
    }  
    if (population > projectedPopulation ) {
        v1.text("OVER");
        //v1.css("color","red");
        //v2.css("background-color","red");
        v2.removeClass("under-capacity");
        v2.addClass("over-capacity");
    } else if (population < projectedPopulation) {
        v1.text("UNDER");
        //v1.css("color","blue");
        //v2.css("background-color","#ff9600");
        v2.removeClass("over-capacity");
        v2.addClass("under-capacity");
    } else {
        v1.text("ON");
        //v1.css("color","black");
        //v2.css("background-color","black");
        v2.removeClass("under-capacity");
        v2.removeClass("over-capacity");
    }
}
function formatInputText(jQueryObject) {
    var i = jQueryObject;
    var v = parseInt(i.val().replace(/[\D]/g, ""));
    i.val(v.formatAsString(0,'.',','));
}

function insertLegend(plot, canvas) {
    var legendContainer = $(".legend", plot.getPlaceholder().parent());
    var series = plot.getData();
    var fragments = [];
    for (var i = 0; i < series.length; ++i) {
        var s = series[i];
        if (!s.label) continue;
        var label = s.label + ' ('+parseFloat(s.percent).toFixed(1)+'%)';
        fragments.push('<div class="legend-item"><div class="legend-color-box" style="background-color:'+s.color+'"></div><div class="legend-label">'+label+'</div></div>');
    }
    if (fragments.length == 0) return;
    legendContainer.html(fragments.join(""));

}

var pieOptions = {
    series: {
        pie: { 
            show: true,
            innerRadius: 0.7,
            stroke: {width:0.000000001},
            highlight: {opacity:0.2},
            label: {
                show: false,
                radius: 1,
                formatter: function(label, slice) {
                    return '<div style="font-size:x-small;text-align:center;padding:2px;color:'+slice.color+';">'+label+' '+Math.round(slice.percent)+'%</div>';
                }
            }
        }
    },
    legend: { show: false 
    },
    grid: {
        hoverable: true
    },
    hooks: {draw: [insertLegend]}
};

function pieHover(container, event, pos, obj) {
    var divHover = $('div.chart-hover');
    if (divHover.length == 0) divHover = $('<div class="chart-hover"><div class="chart-hover-inner"><div class="chart-hover-arrow"></div><div class="chart-hover-text"></div></div></div>').appendTo("body").fadeIn(100);
    
    var offset = container.offset();
    var posX = pos.pageX - offset.left;
    var posY = pos.pageY - offset.top;
    //console.log('x='+posX+',y='+posY);
    //console.log(obj);
    var centerX = container.width()/2;
    var centerY = container.height()/2;
    var minConLen = centerX;
    if (minConLen > centerY) minConLen = centerY;
    var radius = 1 * minConLen;
    var innerRadius = 0.7 * radius;
    
    // test if mouse hover on the valid pie region only
    var sqDist = (centerX - posX) * (centerX - posX) + (centerY - posY) * (centerY - posY);
    if (sqDist <= radius*radius && sqDist >= innerRadius*innerRadius && obj) { 
      var percent = parseFloat(obj.series.percent).toFixed(1);
      var amount = obj.series.data[0][1].formatAsString(0,'.',',');
      $('.chart-hover-text', divHover).html(obj.series.label + '&nbsp;(' + percent + '%)<br/>' + amount + '&nbsp;km<sup>2</sup>');
      divHover.show();
      divHover.offset({left:pos.pageX+15,top:pos.pageY-15});
    } else {
      divHover.hide();
    }
    /*
    var drawingCanvas = $('canvas.overlay', container).get(0);
    if(drawingCanvas.getContext) {
      var angle = obj.series.startAngle+(obj.series.angle/2);
      var context = drawingCanvas.getContext('2d');
      //context.strokeStyle = "transparent";
      context.beginPath();
      context.lineWidth = 1;
      context.strokeStyle = obj.series.color;
      //context.arc(centerX,centerY,innerRadius,obj.series.startAngle,obj.series.startAngle+(obj.series.angle/2),false);
      context.moveTo(centerX,centerY);
      context.lineTo(centerX+innerRadius*Math.cos(angle),centerY+innerRadius*Math.sin(angle));
      context.stroke();
      context.closePath();
    }
    
    if (divHover.length == 0) divHover = $('<div class="chart-hover"></div>').appendTo(container);
    divHover.css("background-color",obj.series.color);
    */
}

function formatOutputData(data) {
    var usageExcessLabels = [
    ["Excess existing cropping","greenyellow"],
    ["Excess existing pasture","#fab019"],
    ["Excess existing non-agric","#ffd900"],
    ["Excess existing infrastructure","#f1eb33"],
    ["Excess existing nature reserve","#bed748"]
    ];
    var usageLabels = [
    ["Food","#a4cf63"],
    ["Biofuel","#6bc27d"],
    ["Textiles","#01aa6f"],
    ["Timber","#00a992"],
    ["Infrastructure","#019482"],
    ["Nature reserve","#018b96"]
    ];
    var usageFoodLabels = [
    ["Red&nbsp;meat","#fab019"],
    ["White&nbsp;meat","#ffd900"],
    ["Dairy","#f1eb33"],
    ["Cereals","#bed748"],
    ["Vegetables","#a4cf63"],
    ["Fruit","#6bc27d"],
    ["Legumes","#01aa6f"],
    ["Nuts&nbsp;&amp;&nbsp;seeds","#00a992"],
    ["Oils","#019482"],
    ["Sweeteners","#018b96"]
    ];
    var usage = [], usageFood = [];
  
    for (var i=0; i<usageExcessLabels.length; ++i) {
        var a = data.excess[i][0];
        if (a > 0) {
            usage.push( {
                label: usageExcessLabels[i][0], 
                color: usageExcessLabels[i][1], 
                data: a
            } );
        }
    }
    for (var i=0; i<usageLabels.length; ++i) {
        var a = data.requirements[10+i][1];  
        if ( a > 0) {
            usage.push( {
                label: usageLabels[i][0], 
                color: usageLabels[i][1], 
                data: a
            } );
        }
    }
    for (var i=0; i<usageFoodLabels.length; ++i) {
        var a = data.requirements[i][1];
        if ( a > 0) {
            usageFood.push( {
                label: usageFoodLabels[i][0], 
                color: usageFoodLabels[i][1], 
                data: a
            } );
        }
    }
    return {
        'usage': usage, 
        'usageFood': usageFood
    };
}

function calculateOutputs() {
    $.post( 'ProcessExcel', $('form#inputForm').serialize(), function(data) {
        $('#outputPopcc').text(data.popcc.formatAsString(0,'.',','));
        var piedata = formatOutputData(data);

        //check wheter are datas existing
        if (piedata.usage.length > 0){   
            pieOptions.legend['container'] = "#chartLandUsageLegend";
            $.plot($("#chartLandUsage"), piedata.usage, pieOptions);
        }
        //if not clear the the legend + piechart
        else{
            $("#chartLandUsage").empty(); 
            $("#chartLandUsageLegend").empty();
        }

        //check wheter are datas existing
        if (piedata.usageFood.length > 0){   
            pieOptions.legend['container'] = "#chartLandUsageFoodLegend";
            $.plot($("#chartLandUsageFood"), piedata.usageFood, pieOptions);
        }
        //if not clear the the legend + piechart
        else{
            $("#chartLandUsageFood").empty(); 
            $("#chartLandUsageFoodLegend").empty(); 
        }

        $("#chartLandUsage").bind("plothover", function(event, pos, obj) {
            pieHover($("#chartLandUsage"), event, pos, obj);
        });

        $("#chartLandUsageFood").bind("plothover", function(event, pos, obj) {
            pieHover($("#chartLandUsageFood"), event, pos, obj);
        });
        updatePopulation();
      
    },'json');
}

$(".tooltip").mouseover(function() {
    alert('works');
});

function initTooltip() {
    var $this = $(this);
    var tooltipElement = $this.next('.tooltip');
    if (tooltipElement.length>0) {
        //console.log(tooltipElement);
        var c = tooltipElement.html();
        if (c.length > 0) {
            $this.qtip({
                content:c,
                position:{
                    target:'mouse',
                    adjust:{
                        x:0,
                        y:10,
                        screen:true
                    }
                },
            show:{
                delay:10,
                solo:true
            },
            style:{
                width:{
                    max:500
                }
            }
            });
//console.log(c);
        }
    }
}

function initHelpDialog($link, $info) {
    if ($info.length > 0) {
        var t = $link.text();
        if (!t) t = $info.attr("title");
        if (!t) t = $link.parent().text();
        $link.click( function(e) {
            e.preventDefault();
            var d = $info.dialog({ modal: true, title: t, width: 455});
            $(".ui-widget-overlay").click (function () {
                d.dialog( "close" );
            });
            return false;
        } );
    }
}

$(document).ready(function() {
    $('#inputPopulation').change(function(){
        formatInputText($(this));
        updatePopulation();
    });
    $('#inputAreasCropping').change(function(){
        formatInputText($(this));
        updateInputAreasTotal();
        calculateOutputs();
    });
    $('#inputAreasPasture').change(function(){
        formatInputText($(this));
        updateInputAreasTotal();
        calculateOutputs();
    });
    $('#inputAreasNonAg').change(function(){
        formatInputText($(this));
        updateInputAreasTotal();
        calculateOutputs();
    });
    $('#inputAreasBuilt').change(function(){
        formatInputText($(this));
        updateInputAreasTotal();
        calculateOutputs();
    });
    $('#inputAreasNature').change(function(){
        formatInputText($(this));
        updateInputAreasTotal();
        calculateOutputs();
    });

    //setup slider panels
    $('.ui-slider-panel').each(function() {
        var $this = $(this);
        var id = $this.attr("id");
        var p = sliderParams[id];
        p["caption"] = p["caption"].toUpperCase();
        p.panel = $this.sliderPanel( p ).change(calculateOutputs);
    });
  
    //use short-term default inputs
    getDefaultInputs("default-inputs-short-term.csv", function() {
        //setup regionSelector
        var stateOptions = $('#regionSelectorState');
        for (var key in regionGroups) {
            var opt = $("<option />").val(key).text(defaultInputs[key].regionName);
            stateOptions.append(opt);
        }
        stateOptions.change();
    });

    $('#regionSelectorState').change(function() {
        var stateId = $(this).val();
        var regionOptions = $('#regionSelectorRegion');
        regionOptions.empty();
        regionOptions.append($("<option />").val(stateId).text("All regions"));
        var list = regionGroups[stateId];
        if (list.length > 0) {
            regionOptions.prop('disabled', false);
            for (var i=0; i<list.length; ++i) {
                regionOptions.append($("<option />").val(list[i]).text(defaultInputs[list[i]].regionName));
            }
        } else {
            regionOptions.prop('disabled', true);
        //regionOptions.disabled = true;
        }
        updateInputValues(stateId);
        calculateOutputs();
    });
    
    $('#regionSelectorRegion').change(function() { 
        updateInputValues($(this).val());
        calculateOutputs();
    });
    
    var updateAfterDefaultChange = function() {
        updateInputValues($('#regionSelectorRegion').val());
        calculateOutputs();
    };
    $('#updateButtonShort').click(function() {
        getDefaultInputs("default-inputs-short-term.csv", updateAfterDefaultChange);
    });
    
    $('#updateButtonLong').click(function() { 
        getDefaultInputs("default-inputs-long-term.csv", updateAfterDefaultChange);
    });

    //setup tooltips
    /*
    $('.param-group .heading').each(initTooltip);
    $('.subheading').each(initTooltip);
    $('#inputAreas label').each(initTooltip);
    $('.ui-slider-panel').each(initTooltip);
    $('#outputCapacity').each(initTooltip);
    $('#outputCapacityPercentage').each(initTooltip);
    */
   
    $('a.help-link').each( function() {
        var $this = $(this);
        var $info = $this.next('.help-info');
        if ($info.length == 0) {
          if ($this.hasClass("label-caption")) {
              $info = $this.closest(".ui-slider-panel").next('.help-info');
          } else {
              $info = $this.parent().next('.help-info');
          }
        }
        initHelpDialog($this, $info);
    });
});


//read default inputs
function getDefaultInputs(filename, onSuccess) {    
    $.ajax({
        type: "GET",
        url: filename,
        dataType: "text",
        success: function(data) {
            defaultInputs = CsvToObjects(data);
            defaultInputs.splice(0,0,undefined); //add empty array element at the front
            onSuccess();
        }
    });
}