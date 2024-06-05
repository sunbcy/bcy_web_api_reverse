const cryptoJS = require("crypto-js")

var Es = "pW8jg/mke6cO1F4CTuaiswhZfQGzMyq5NJRLPVIvDxlA7=E3YrSUoH0b2BXKn9td+";

function Bs(e) {
    var s, o, i, a, l, r, c, u, f = 0, h = "", m = {
        UvJUa: "0|6|2|4|7|5|1|8|3"
    };
    do {
        for (var y = m["UvJUa"].split("|"), g = 0; ; ) {
            switch (y[g++]) {
            case "0":
                s = e[f++];
                continue;
            case "1":
                r = 63 & u >> 6;
                continue;
            case "2":
                i = e[f++];
                continue;
            case "3":
                h += Es["charAt"](a) + Es["charAt"](l) + Es["charAt"](r) + Es["charAt"](c);
                continue;
            case "4":
                u = ((s << 16) | (o << 8)) | i;
                continue;
            case "5":
                l = u >> 12 & 63;
                continue;
            case "6":
                o = e[f++];
                continue;
            case "7":
                a = u >> 18 & 63;
                continue;
            case "8":
                c = u & 63;
                continue
            }
            break
        }
    } while (f < e.length);
    var v = e.length % 3;
    return h + "===".slice(v || 3);
}

function Fs(e, t) {
    return e.charCodeAt(Math.floor(t % e.length));
}

function qs(e, t) {
    const a = t.split("");
    return a.map(function(t, a) {
        return t.charCodeAt(0) ^ Fs(e, a + 1 - 1)
    })
}

function encrypt_token(e) {
    // var format_dict = {"type":"YQD","text":e,"page":1,"v":"beta","_t":1706099652039}
    console.log(e)
    const t = "yGz4n9XE9xYy2Oj5Ub7E6u9a5p5aIWZYe53Orq5wE5UgnjbWq0410WTvmLBO1Z2N";
    const a = qs(t.toString(), e.toString());
    return "20230327." + cryptoJS.MD5(Bs(a));
}

// console.log(encrypt_token({"type": "YQM", "text": "周深 baby", "page": 1, "v": "beta", "_t": 1716266332026}))  //  'token': '20230327.054aa0c40a3e075f25db2b7105685462'
console.log(encrypt_token(
    encodeURIComponent(JSON.stringify(
        {
            type: "YQM",
            text: "周深 baby",
            page: 1,
            v: "beta",
            _t: 1716266332026
        }
    ))
))
// console.log(JSON.stringify(
//         {
//             type: "YQD",
//             text: "周深 baby",
//             page: 1,
//             v: "beta",
//             _t: 1706099652039
//         }
//     ))
// console.log(encrypt_token('周深 baby'))