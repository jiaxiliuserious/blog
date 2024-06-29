Vue.component('chat-messages', {
    props: ['messages'],
    template: `
        <div>
            <br>
            <div v-for="message in messages" style="border-bottom: 2px solid black; margin: 20px 0;">
                <p>{{message.tip}}:{{ message.message }}</p>
            </div>
        </div>
    `
});

new Vue({
    el: '#app',
    data: {
        // 历史信息
        messages: [],
        // 用户输入信息
        newMessage: ''
    },
    methods: {
        sendMessage: function() {
            let usermes = {tip:"用户",message:this.newMessage};
            this.messages.push(usermes);
            axios.post('', {message: this.newMessage})
                .then(response => {
                    // 响应加入历史信息
                    this.messages.push({tip:"GPT",message:response.data.message});
                })
                .catch(error => {
                    console.error(error);
                });
            // 重置输入信息
            this.newMessage = '';
        }
    }
});
