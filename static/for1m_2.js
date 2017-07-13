/**
 * Created by Keepair on 2017-07-12.
 */
$(document).ready(function () {
        var lastId = -1;
        var earlyId = -1;
        var days = 1000*60*60*24;
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

        //###########################################################
        if ($(".timePTag").length) {
            $(".timePTag").each(function(index) {
                var now = new Date;
                var id = $(this).attr("id");

                var sourcedate = new Date(id);
                var timestamp = Math.floor((now - sourcedate) /days);
                if (timestamp>=30){
                    $(this).text('Expired');
                    $(this).parent().parent().removeClass("animaEmerge").addClass("Expired");
                }
                else {
                    $(this).text((timestamp)+'days ago');
                }
             });
        }
        else {
        }
        //###########################################################

        $("#submitBtn").click(function () {
            var getText = $("#submitTextarea").val();
            if (getText.length >= 200){
                $.ajax({
                url:"/month/list/",
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
                                '<div class="panel panel-primary anima"><div class="panel-body animaEmerge panelheightauto">'+value.text+'</div><div class="panel-footer panel-custom text-right panelheightauto">'+ '<p class="timePTag" id="'+value.createdAt+'">'+'<span class="glyphicon glyphicon-time"></span>'+'</p>'+'</div></div>'
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
                            var timestamp = Math.floor((now - sourcedate) /days);
                            if (timestamp>=30){
                            $(this).text('Expired');
                            $(this).parent().parent().removeClass("animaEmerge").addClass("Expired");
                            }
                            else {
                            $(this).text((timestamp)+'days ago');
                            }
                            });
                            }
                            else {
                        }
                     }
                });

            }
            else {
                alert("Would you write anything more, Please?! min : 200 max : 5000")
            }

        });
        //###########################################################

        $("#refreshBtn").click(function (e) {
                    $.ajax({
                    url:"/month/list/",
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
                                '<div class="panel panel-primary anima"><div class="panel-body animaEmerge panelheightauto">'+value.text+'</div><div class="panel-footer panel-custom text-right panelheightauto">'+ '<p class="timePTag" id="'+value.createdAt+'">'+'<span class="glyphicon glyphicon-time"></span>'+'</p>'+'</div></div>'
                                );

                            lastId = value.id;

                        });

                        scrollTo(0,0);

                        if ($(".timePTag").length) {
                        $(".timePTag").each(function(index) {
                        var now = new Date;
                        var id = $(this).attr("id");

                        var sourcedate = new Date(id);
                        var timestamp = Math.floor((now - sourcedate) /days);
                        if (timestamp>=30){
                        $(this).text('Expired');
                        $(this).parent().parent().removeClass("animaEmerge").addClass("Expired");
                        }
                        else {
                        $(this).text((timestamp)+'days ago');
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
                url:'/month/list/',
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
                        '<div class="panel panel-primary anima"><div class="panel-body animaEmerge panelheightauto">'+value.text+'</div><div class="panel-footer panel-custom text-right panelheightauto">'+ '<p class="timePTag" id="'+value.createdAt+'">'+'<span class="glyphicon glyphicon-time"></span>'+'</p>'+'</div></div>'
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
                    var timestamp = Math.floor((now - sourcedate) /days);
                    if (timestamp>=30){
                    $(this).text('Expired');
                    $(this).parent().parent().removeClass("animaEmerge").addClass("Expired");
                    }
                    else {
                    $(this).text((timestamp)+'days ago');
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