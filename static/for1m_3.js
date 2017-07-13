/**
 * Created by Keepair on 2017-07-13.
 */

    $(document).ready(function () {

        $.ajax({
            type : 'get',
            url :'/mainStatus/',
            datatype : 'json',
            cache : false,
            success : function (data) {
                var array = ['all', 'ara', 'ben', 'chi', 'eng', 'fre', 'ger', 'hin', 'jap', 'jav', 'kor', 'lah', 'mal', 'por', 'rus', 'spa', 'tel']
                for (var i=0; i<data.length; i++){
                    var text = array[i]+'Status';
                    if(data[i]==0){
                        $('#'+text).text("Nobody here")
                    }
                    else if(data[i]<10){
                        $('#'+text).text("♥")
                    }else if(data[i]<20){
                        $('#'+text).text("♥◆")
                    }else if(data[i]<40){
                        $('#'+text).text("♥◆♣")
                    }else if(data[i]<80){
                        $('#'+text).text("♥◆♣♠")
                    }else if(data[i]<160) {
                        $('#'+text).text("♥◆♣♠★")
                    }else if(data[i]<320){
                        $('#'+text).text("♥◆♣♠★♬")
                    }else {
                        $('#'+text).text("♥◆♣♠★♬!!")
                    };
1                }
            }
        });

    });