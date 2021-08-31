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
    $(function () {
        var getMessageText, message_side, sendMessageLeft, sendMessageRight;
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
        $('.send_message').click(function (e) {
            $.ajax({
            url: "/",
            success: display_news
        });

        console.log("Au revoir");
        
        function display_news(result){
            console.log("Nous allons afficher les articles de presse");
        }
            return sendMessageRight(getMessageText());

        });
        $('.message_input').keyup(function (e) {
            if (e.which === 13) {
                $.ajax({
            data: {
                question_input: $("#input_request").val()
            },
            type: 'POST',
            url: "/process",
            success: display_news
        })
        .done(function(data) {
            console.log(data.question_input)
        });


        console.log("Au revoir");
        
        function display_news(result){
            console.log("Nous allons afficher les articles de presse");
        }
                return sendMessageRight(getMessageText());
            }
        });
        sendMessageLeft("salut mon ptit! Que puis-je faire pour toi? :)");
    });
}.call(this));

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
