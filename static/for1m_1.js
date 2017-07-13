
    $(document).ready(function () {
        var lastId = -1;
        var earlyId = -1;
        var endSentence = $(".hiddenInfo").attr("id");
        var seconds = $(".hiddenInfoTwo").attr("id");
        var language = '/'+$(".hiddenInfoThree").attr("id")+'/';
        if ($(".hiddenId").length) {
                $(".hiddenId").each(function(index) {
                    if (earlyId == -1|| earlyId > $(this).attr("id")){
                        earlyId = $(this).attr("id");
                    }
                    if (lastId == -1|| lastId < $(this).attr("id")){
                        lastId = $(this).attr("id");
                    }
                 });
            }
            else {
            }
        //###########################################################
        setInterval(function() {
            if ($(".timePTag").length) {
                $(".timePTag").each(function(index) {
                    var now = new Date;
                    var id = $(this).attr("id");
                    var sourcedate = new Date(id);
                    var timestamp = Math.floor((now - sourcedate) /1000);
                    if (timestamp>=60){
                        $(this).text(endSentence);
                        $(this).parent().parent().removeClass("animaEmerge").addClass("Expired");
                    }
                    else {
                        $(this).text((60-timestamp)+seconds);
                    }
                 });
            }
            else {
            }
        }, 1000);
        $("#submitBtn").click(function () {
            var getText = $("#submitTextarea").val();
            if (getText != ''){
                $.ajax({
                url:language,
                type:"post",
                data:{
                    l : lastId,
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
                     }
                });

            }
            else {
                alert("Would you write any sentences. Please?!")
            }

        });

        $("#refreshBtn").click(function (e) {
                    $.ajax({
                    url:language,
                    type:"get",
                    data:{
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
                }
            });
        e.preventDefault();
        });


        $("#moreLoadBtn").click(function (e) {
                    $.ajax({
                    url:language,
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
                        window.scrollTo(0,document.body.scrollHeight);
                       }
                    });
                    e.preventDefault();
                });

    });