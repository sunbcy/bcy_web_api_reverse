window=global;
const CryptoJS=require('crypto-js')
function Fs(e, t) {
    return e['charCodeAt'](Math['floor']({
        ELxvT: function(e, t) {
            return e % t
        }
    }["ELxvT"](t, 64)))
}
function qs(e, t) {
      a = t['split']("")
      , l = 114514;
        l = 1;
    return a['map']((function(t, a) {
        // const r = n;
        return t['charCodeAt'](0)^Fs( e, (a+ l) - 1)
    }
    ))
}
function Bs(e) {
    // m = {
    //     HPrAi: $s(451, "%amn"),
    //     UvJUa: $s(384, 'n8^Y'),
    //     lPeqS: $s(422, 'soEi'),
    // }
    f = 0, h = "";
    do {
        for (var y = '0|6|2|4|7|5|1|8|3'['split']("|"), g = 0; ; ) {
            switch (y[g++]) {
            case "0":
                s = e[f++];
                continue;
            case "1":
                r = 63 & (u>> 6);
                continue;
            case "2":
                i = e[f++];
                continue;
            case "3":
                Es='pW8jg/mke6cO1F4CTuaiswhZfQGzMyq5NJRLPVIvDxlA7=E3YrSUoH0b2BXKn9td+';
                h += ((Es['charAt'](a)+ Es['charAt'](l))+Es['charAt'](r)) + Es['charAt'](c);
                continue;
            case "4":
                u = s<<16|o<< 8| i;
                continue;
            case "5":
                l = u>>12&63;
                continue;
            case "6":
                var o;
                o = e[f++];
                continue;
            case "7":
                a = u>>18&63;
                continue;
            case "8":
                c = u&63;
                continue
            }
            break
        }
    } while (f < e['length']);
    var v = (e['length']% 3);
    return (v ? h['slice'](0, (v-3)) : h)
}
let t='yGz4n9XE9xYy2Oj5Ub7E6u9a5p5aIWZYe53Orq5wE5UgnjbWq0410WTvmLBO1Z2N'
// e='{"type":"YQM","text":"红色高跟鞋","page":1,"v":"beta","_t":1708266541189}'
// e=encodeURIComponent(e);
// console.log(e)
let e='%7B%22id%22%3A%22m3f63OtUGNZoMDio1KqoFvz5tn8-QIvMrKHzz2lA7dWSL0qLZFeLha7sr2xvLdJo%22%2C%22quality%22%3A%22128%22%2C%22_t%22%3A%221708331090368%22%7D'
// var a=qs(t["toString"](), e['toString']())
// console.log(a.length)
// console.log()
// token=CryptoJS.MD5(Bs(a)).toString();
// console.log("20230327."+token)
function get_token(t,e){
    let data = Bs(qs(t["toString"](), e['toString']()))
    return CryptoJS.MD5(data).toString()
}

console.log(get_token(t,e))
console.log( Bs(qs(t["toString"](), e['toString']())))
// b3f634HzOLrfMF9SfoFY6YVXPExJXlsqDmWF8caIOg6ByR2n2
function get_music_token(t,e){
    let data = Bs(qs(t["toString"](), e['toString']()))+'=='
    return CryptoJS.MD5(data).toString()
}
console.log(get_music_token(t,e))
console.log( Bs(qs(t["toString"](), e['toString']()))+'==')