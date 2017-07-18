
    $(document).ready(function () {
        var lastId = -1;
        var timeUnit;
        var unitMath;
        var stampLine;
        var postId = $(".hiddenHOM").attr("title");
        var usingUrl;


        if ($(".hiddenCommentId").length) {
                $(".hiddenCommentId").each(function() {
                    lastId = $(this).attr("id")
                 });
            }
        else {
        }
        if($(".hiddenHOM").attr("id")=='month'){
            timeUnit = 'days ago';
            unitMath = 1000*60*60*24;
            stampLine = 30;
            usingUrl = '/comment/month/';
        }
        else {
            timeUnit = 'min ago';
            unitMath = 1000*60;
            stampLine = 60;
            usingUrl = '/comment/hour/';
        }

        //###########################################################
        if ($(".timePTag").length) {
            $(".timePTag").each(function() {
                var now = new Date;
                var id = $(this).attr("id");

                var sourcedate = new Date(id);
                var timestamp = Math.floor((now - sourcedate) /unitMath);
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
            if (getText != ''){
                $.ajax({
                url:usingUrl,
                type:"post",
                data:{
                    l : lastId,
                    p : postId,
                    c : getText,
                },
                dataType:"json",
                cache : false,
                success : function (data) {
                        $.each(data, function (index, value) {
                            $("#contentsbox")
                                .append(
                                    '<div class="row"><div class="col-lg-6 col-lg-offset-3 col-md-6 col-md-offset-3 col-sm-8 col-sm-offset-2 col-xs-12 commentBody animaEmerge"><div class="row"><div class="col-lg-12 col-md-12 col-sm-12 col-xs-12 text-left wordBreak commentFooter">'+value.text+'<p class="timePTag text-right commentTimePTag" id="'+value.createdAt+'"><span class="glyphicon glyphicon-time"></span></p></div><span class="hiddenCommentId" hidden="true" id="'+value.id+'"></span></div></div></div>'
                                );
                            if (lastId<value.id){
                            lastId = value.id;
                            }
                        });
                        window.scrollTo(0,document.body.scrollHeight);

                        $("#writeModal").hide();
                        $("#submitTextarea").val('');

                        if ($(".timePTag").length) {
                        $(".timePTag").each(function() {
                            var now = new Date;
                            var id = $(this).attr("id");

                            var sourcedate = new Date(id);
                            var timestamp = Math.floor((now - sourcedate) /unitMath);
                            if (timestamp>stampLine){
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
                alert("Would you write anything")
            }

        });
    });