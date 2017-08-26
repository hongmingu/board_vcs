$(document).ready(function () {
        var lastId = -1;
        var earlyId = -1;
        var timeMath;
        var timeUnit;
        var stampLine;
        var usingUrl = $(".hiddenHOM").val();


        if ($(".hiddenId").length) {
                $(".hiddenId").each(function(index) {
                    if (earlyId == -1|| earlyId>$(this).attr("id")){
                        earlyId = $(this).attr("id");
                    }
                    if (lastId == -1|| lastId<$(this).attr("id")){
                        lastId = $(this).attr("id");
                    }
                 });
            }
        else {
        }

        if($(".hiddenHOM").attr("id")=='month'){
            timeUnit = 'days ago';
            timeMath = 1000*60*60*24;
            stampLine = 30;
        }
        else {
            timeUnit = 'min remains';
            timeMath = 1000*60;
            stampLine = 60;
        }
        //###########################################################
        if ($(".timePTag").length) {
            $(".timePTag").each(function(index) {
                var now = new Date;
                var id = $(this).attr("id");

                var sourcedate = new Date(id);
                var timestamp = Math.floor(60- (now - sourcedate) /timeMath);
                if (timestamp>=stampLine){
                    $(this).text('Expired');
                    $(this).parent().parent().removeClass("animaEmerge").addClass("Expired");
                }
                else {
                    $(this).text((timestamp)+timeUnit);
                }
             });
        }
        else {
        }
        //###########################################################

        $("#submitBtn").click(function () {
            var getText = $("#submitTextarea").val();
            getText.replace(/</g, "&lt;").replace(/>/g, "&gt;");
            if (getText.length >= 50){
                $.ajax({
                url:usingUrl,
                type:"post",
                data:{
                    l : lastId,
                    e : earlyId,
                    t : "submitBtn",
                    c : getText,
                },
                dataType:"json",
                cache : false,
                success : function (data) {
                        $.each(data, function (index, value) {
                            $("#contentsbox")
                                .prepend(
                                    '<div class="row paddingTop10"><a href="'+value.id+'"><div class="col-lg-6 col-lg-offset-3 col-md-6 col-md-offset-3 col-sm-8 col-sm-offset-2 col-xs-12 animaEmerge"><div class="row"><div class="col-lg-12 col-md-12 col-sm-12 col-xs-12 text-left textBoxBody wordBreak"><p><h5>'+value.title+'</h5></p></div><div class="col-lg-12 col-md-12 col-sm-12 col-xs-12 text-right textBoxFooter"><p class="timePTag" id="'+value.createdAt+'"><span class="glyphicon glyphicon-time"></span>></p></div></div></div></a></div>'
                                );

                            lastId = value.id;
                        });

                        scrollTo(0,0);

                        $("#writeModal").hide();
                        $("#submitTextarea").val('');
                        if ($(".timePTag").length) {
                        $(".timePTag").each(function(index) {
                            var now = new Date;
                            var id = $(this).attr("id");

                            var sourcedate = new Date(id);
                            var timestamp = Math.floor(60-(now - sourcedate) /timeMath);
                            if (timestamp>=stampLine){
                            $(this).text('Expired');
                            $(this).parent().parent().removeClass("animaEmerge").addClass("Expired");
                            }
                            else {
                            $(this).text((timestamp)+timeUnit);
                            }
                            });
                            }
                            else {
                        }
                     }
                });

            }
            else {
                alert("Would you write anything more, Please?! min : 50 max : 5000")
            }

        });
        //###########################################################

        $("#refreshBtn").click(function (e) {
                    $.ajax({
                    url:usingUrl,
                    type:"get",
                    data:{
                    e : earlyId,
                    l : lastId,
                    t : 'refreshBtn',
                    },
                    dataType : "json",
                    cache : false,
                    success : function (data) {
                        $.each(data, function (index, value) {
                            $("#contentsbox")
                                .prepend(
                                    '<div class="row paddingTop10"><a href="'+value.id+'"><div class="col-lg-6 col-lg-offset-3 col-md-6 col-md-offset-3 col-sm-8 col-sm-offset-2 col-xs-12 animaEmerge"><div class="row"><div class="col-lg-12 col-md-12 col-sm-12 col-xs-12 text-left textBoxBody wordBreak"><p><h5>'+value.title+'</h5></p></div><div class="col-lg-12 col-md-12 col-sm-12 col-xs-12 text-right textBoxFooter"><p class="timePTag" id="'+value.createdAt+'"><span class="glyphicon glyphicon-time"></span></p></div></div></div></a></div>'
                                );

                            lastId = value.id;

                        });

                        scrollTo(0,0);

                        if ($(".timePTag").length) {
                        $(".timePTag").each(function(index) {
                        var now = new Date;
                        var id = $(this).attr("id");

                        var sourcedate = new Date(id);
                        var timestamp = Math.floor(60-(now - sourcedate) /timeMath);
                        if (timestamp>=stampLine){
                        $(this).text('Expired');
                        $(this).parent().parent().removeClass("animaEmerge").addClass("Expired");
                        }
                        else {
                        $(this).text((timestamp)+timeUnit);
                        }
                        });
                        }
                        else {
                        }
                    }

            });
        e.preventDefault();
        });


       $("#moreLoadBtn").click(function (e) {
                $.ajax({
                url:usingUrl,
                type:"get",
                data:{
                e : earlyId,
                t : 'moreLoad',
                },
                dataType : "json",
                cache : false,
                success : function (data) {
                    $.each(data, function (index, value) {
                        $("#contentsbox")
                        .append(
                            '<div class="row paddingTop10"><a href="'+value.id+'"><div class="col-lg-6 col-lg-offset-3 col-md-6 col-md-offset-3 col-sm-8 col-sm-offset-2 col-xs-12 animaEmerge"><div class="row"><div class="col-lg-12 col-md-12 col-sm-12 col-xs-12 text-left textBoxBody wordBreak"><p><h5>'+value.title+'</h5></p></div><div class="col-lg-12 col-md-12 col-sm-12 col-xs-12 text-right textBoxFooter"><p class="timePTag" id="'+value.createdAt+'"><span class="glyphicon glyphicon-time"></span></p></div></div></div></a></div>'
                        );
                        if (earlyId > value.id){
                        earlyId = value.id;
                        }
                    });
                    if ($(".timePTag").length) {
                    $(".timePTag").each(function(index) {
                    var now = new Date;
                    var id = $(this).attr("id");

                    var sourcedate = new Date(id);
                    var timestamp = Math.floor(60-(now - sourcedate) /timeMath);
                    if (timestamp>=stampLine){
                    $(this).text('Expired');
                    $(this).parent().parent().removeClass("animaEmerge").addClass("Expired");
                    }
                    else {
                    $(this).text((timestamp)+timeUnit);
                    }
                    });
                    }
                    else {
                    }
                    window.scrollTo(0,document.body.scrollHeight);
                   }
                });
                e.preventDefault();
            });

    });