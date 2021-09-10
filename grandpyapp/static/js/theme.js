(function () {
    var Message;
    Message = function (arg) {
        this.text = arg.text, this.message_side = arg.message_side;
        this.draw = function (_this) {
            return function () {
                var $message;
                $message = $($('.message_template').clone().html());
                $message.addClass(_this.message_side).find('.text').html(_this.text);
                $('.messages').append($message);
                return setTimeout(function () {
                    return $message.addClass('appeared');
                }, 0);
            };
        }(this);
        return this;
    };



    var Google_Map;
    Google_Map = function (arg) {
        this.text = arg.text, this.message_side = arg.message_side;
        this.draw = function (_this) {
            return function () {
                var $message;
                $message = $($('.message_template_map').clone().html());
                $message.addClass(_this.message_side).find('.text').html(_this.text);
                $('.messages').append($message);
                return setTimeout(function () {
                    return $message.addClass('appeared');
                }, 0);
            };
        }(this);
       return this;
    };



    $(function () {
        var getMessageText, message_side, sendMessageLeft, sendMessageRight, sendMessageMap;
        message_side = 'right';
        getMessageText = function () {
            var $message_input;
            $message_input = $('.message_input');
            return $message_input.val();
        };
        sendMessageRight = function (text) {
            var $messages, message;
            if (text.trim() === '') {
                return;
            }
            $('.message_input').val('');
            $messages = $('.messages');
            message_side = 'right';
            message = new Message({
                text: text,
                message_side: message_side
            });
            message.draw();
            return $messages.animate({ scrollTop: $messages.prop('scrollHeight') }, 300);
        };
        sendMessageLeft = function (text) {
            var $messages, message;
            if (text.trim() === '') {
                return;
            }
            $('.message_input').val('');
            $messages = $('.messages');
            message_side = 'left';
            message = new Message({
                text: text,
                message_side: message_side
            });
            message.draw();
            return $messages.animate({ scrollTop: $messages.prop('scrollHeight') }, 300);
        };


        sendMessageMap = function (text) {
            var $messages, message;
            $('.message_input').val('');
            $messages = $('.messages');
            message_side = 'left';
            message = new Google_Map({
                text: text,
                message_side: message_side
            });
            message.draw();
            return $messages.animate({ scrollTop: $messages.prop('scrollHeight') }, 300);
        };

        
        $('.send_message').click(function (e) {
            $.ajax({
            data: {
                question_input: $("#input_request").val()
            },
            type: 'POST',
            url: "/process",
        })
        .done(function(data) {

            console.log(data.wiki_input)
            sendMessageLeft(data.question_input)
            sendMessageMap()
            
            $("#map:first").attr("id","map"+($(".map").length))
            sendMessageLeft(data.wiki_input)
            let map_creation= 1;
            if(map_creation){
                // Initialize and add the map
                setTimeout(function initMap() {
                // The location of target_search
                let target_search = { lat: data.latitude_input, lng: data.longitude_input };
                // The map, centered at target_search
                let map = new google.maps.Map(document.getElementById("map"+($(".map").length)), {
                    zoom: 8,
                    center: target_search,
                });
                // The marker, positioned at target_search
                let marker = new google.maps.Marker({
                    position: target_search,
                    map: map,
                });
                },1000);
                //Change id of first balise map in html
                // setTimeout($("#map:first").attr("id","mapold"), 10000) ;
            }
            i=i++;
            }
        );

        console.log("Au revoir");
        

            return sendMessageRight(getMessageText());

        });
        $('.message_input').keyup(function (e) {
            if (e.which === 13) {
                $.ajax({
            data: {
                question_input: $("#input_request").val()
            },
            type: 'POST',
            url: "/process"
        })
        .done(function(data) {
            sendMessageLeft(data.question_input);
        })

        //.fail(sendMessageLeft("je n'ai pas compris. Peut être que si tu m'apportes une petite culotte cela m'aidera à me souvenir"));

            return sendMessageRight(getMessageText());
            }
        });
        sendMessageLeft("salut mon ptit! Que puis-je faire pour toi? :)");
    });
}.call(this));


//fonction exemple pour test et comprendre le fonctionnement d'ajax
$(document).ready(function(){
    console.log("bonjour");
        
        $.ajax({
            url: "/",
            success: display_news
        });

        console.log("Au revoir");
        
        function display_news(result){
            console.log("Nous allons afficher les articles de presse");
        }
    });


//function initMap() {
  // The location of target_search
//  let target_search = { lat: -25.344, lng: 131.036 };
  // The map, centered at target_search
//  let map = new google.maps.Map(document.getElementById("map"), {
//    zoom: 6,
//    center: target_search,
//  });
  // The marker, positioned at target_search
//  let marker = new google.maps.Marker({
//    position: target_search,
//    map: map,
//}
            //let python_data_lat = {{ lat | tojson }};
            //let python_data_lon = {{ lon | tojson }};