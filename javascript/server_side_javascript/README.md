## server_side_javascript

[뒤로가기](/javascript/README.md)

자바스크립트가 웹 브라우저에 어떻게 내장되는지를 설명하고, 각 웹브라우저가 자기 나름의 방식대로 확장한 자바스크립트 API를 다룬다. 자바스크립트는 웹 프로그래밍에 사용되는 언어이고, 대다수 자바스크립트 코드는 웹브라우저에서 돌아가도록 작성된다.하지만 자바스크립트는 빠르며, 일반적인 용도로 사용하기에도 부족함이 없는 프로그래밍 언어이기 때문에, 자바스크립트를 웹브라우저 외의 다른 프로그래밍 작업에도 충분히 사용할 수 있다.

여기서는 2가지 클라이언트측 자바스크립트 라이노와 노드를 살펴보고 있고, 전체적인 설명은 진행하며, 약간의 예시들은 nodejs만 진행할 예정입니다.

라이노(Rhino)는 자바로 작성된 자바스크립트 인터프리터이고, 자바스크립트 프로그램에서 자바 API를 모두 사용할 수 있게 한다.
노드(Node)는 구글의 V8 자바스크립트 인터프리터를 기반으로 하고, POSIX(Unix) API(파일, 프로세스, 스트림, 소켓, 기타 등등)에 대한 저수준 바인딩을 제공하며 특히 비동기 I/O,네트워킹,HTTP처리를 특징으로 하고 있다.
보통 노드와 라이노는 둘 다 서버를 만들거나 서버에서의 스크립트 처리를 위해 사용된다. 하지만 '서버 측' 이라는 문구에는 '웹 브라우저 이외의 모든 것' 이라는 의미도 있다. 라이노 프로그램으로는 자바의 스윙 프레임워크를 사용하여 그래픽 UI를 만들 수도 있고, 노드로는 셸 스크립트와 같은 방식으로 파일을 처리하는 스크립트 프로그램을 실행할 수도 있다.

###노드를 사용한 비동기 I/O
노드는 C++로 작성된 빠른 자바스크립트 인터프리터로 프로세스, 파일, 네트워크 소켓 등과 관련한 저수준 유닉스 API,HTTP 클라이언트, 그리고 서버 API에 대한 바인딩을 포함하고 있다. 특별한 이름이 붙은 동기화 메서드 몇 개를 제외하면 노드의 모든 바인딩은 비동기적이다. 그리고 기본적으로 노드 프로그램은 블로킹 되지 않는데, 이는 일반적으로 스케일을 확장하는 데 유리하며 고부하를 효율적으로 처리할 수 있음을 뜻한다. API가 비동기적이기 때문에 노드는 이벤트 핸들러로 API 결과를 처리하고, 이러한 이벤트 핸들러는 보통 중첩 함수와 클로저로 구현된다.
여기서 노드에 가장 중요한 API와 몇가지 이벤트를 강조하여 다루지만, 노드 전체를 다룰 수는 없다.
```
//브라우저와 마찬가지로 노드는 디버그 출력을 위한 console.log를 정의한다.
console.log("Hello Node");					->콘솔에 디버깅 메세지를 출력한다.

//load() 대신 require()를 사용하라.require()는 지정된 모듈을 불러와서 단 한 번만 실행한다. 
//그리고 erported기호가 있는 객체를 반환한다.
var fs = require("fs");						->fs 모듈을 불러오고 모듈의 API 객체를 반환한다.
```
노드의 전역 객체에는 표준 ECMAScript 5의 생성자, 프로퍼티, 함수가 모두 구현되어 있다. 추가로 클라이언트 측 타이머 함수인 setTimeout()과 setInterval(), clearTimeout(), clearInterval()도 지원한다.
```
//1초 후에 "Hello World"를 출력한다.
setTimeout(function() { console.log("Hello World"); }, 1000);
```
노드에서 구현한 방식은 웹브라우저의 구현과 호환된다.
노드는 process 네임스페이스에 또 다른 중요한 전역 객체들을 정의하고 있다. 다음은 process 네임스페이스의 몇 가지 프로퍼티들이다.
```
precess.version							->노드 버전 문자열
precess.argv							->argv[0]는 "node"인 명령줄 인자
precess.env								->환경 변수 객체. 예) precess.env.PATH
precess.pid								->프로세스 id
precess.getuid()						->사용자 id를 반환함
precess.cwd()							->현재 작업 디렉터리를 반환함
precess.chdir()							->디렉터리를 바꿈
precess.exit()							->종료 (종료 후크를 실행하고 난 후에)
```
노드의 함수와 메서드는 비동기적이기 때문에, 함수와 메서드의 실행이 완료되기를 기다리는 동안 프로그램은 블로킹 되지 않는다. 따라서 논블로킹 메서드의 반환 값을 통해서는 비동기 작업의 결과를 얻을 수 없다. 
만약 비동기 작업의 결과를 얻고 싶거나 언제 작업이 완료되는지를 알고 싶다면, 반환 값이 준비되었을 때 또는 작업이 완료되었을 때(또는 에러가 발생했을 때) 노드가 호출할 수 있는 **콜백** 함수를 제공해야 한다. 즉, **setTimeout() 같은 함수에 콜백 함수를 전달하면 모드는 적합한 시점에 그 함수를 호출해 줄 것이다** 그 방법을 사용할 수 없는 경우에는 노드의 이벤트 기반 구조를 활용하는 방법도 있다.
이벤트를 발생시키는 노드 객체 event emitter는 이벤트 핸들러를 등록할 수 있는 on() 메서드를 갖고 있다. 그 첫 번째 인자로는 이벤트 형식(문자열)을 전달하고 두 번째 인자로는 핸들러 함수를 전달한다. 이벤트의 형식(문자열)을 전달하고 두 번째 인자로 핸들러 함수를 전달한다. 이벤트의 형식, 즉 종류에 따라 핸들러 함수에 전달되는 인자도 달라진다. 그러니 핸들러를 작성하는 방법을 정확하게 알고 싶다면 API 문저를 참고하기 바란다.
```
emitter.on(name, f)								->이미터에서 발생한 name 이벤트를 처리하는 f를 등록
emitter.addListener(name, f)					->addListener()는 on()과 같다.
emitter.once(name, f)							->한 번만 실행된다. 그런 다음 f는 자동으로 제거된다.
emitter.listeners(name)							->핸들러 함수 배열을 반환한다.
emitter.removeListener(name, f)					->이벤트 핸들러 f를 해제한다.
emitter.removeAllListeners(name)				->name 이벤트에 대한 모든 핸들러를 제거한다.
```
앞서 보여준 process 객체는 이벤트 이미터다. 여기서 precess의 이벤트를 처리하는 몇가지 예제가 있다.
```
//"exit" 이벤트는 노드가 종료하기 전에 발생한다.
process.on("exit", function() { conosole.log("Godd bye"); });

//핸들러가 등록된 경우 캐치되지 않은 예외는 이벤트를 발생시킨다.
//그렇지 않으면 노드를 예외를 출력하고 종료한다.
process.on("uncaughtException", function(e) { console.log(Exception, e); });

//SIGINT, SIGHUP 그리고 SIGTERM 같은 POSIX 신호는 이벤트를 발생시킨다.
process.on("SIGINT", function() { console.log("Ctrl-C는 무시함"); });
```
노드가 고성능 I/O를 위해 설계되었기 때문에, 그 API 가운데 가장 널리 쓰이는 것 중 하나가 바로 스트림 API다. 읽기 스트림은 데이터가 도착하면 이벤트를 발생시킨다. 다음에 나온 코드에서 s는 읽기 스트림이고 어딘가에서 미리 획득되었다고 가정한다. 파일과 네읕워크 소켓에 대한 스트림 객체를 어떻게 얻을 수 있는지는 나중에 살펴본다.
```
//입력 스트림 s:
s.on("data", f);							->데이터를 사용할 수 있게 되면 f()의 인자로 데이터를 전달한다.
s.on("end", f);								->데이터가 더 도착하지 않을 때 EOF에서 "end" 이벤트가 발생한다.
s.on("error", f);							->뭔가 잘못되면 예외 f()로 전달한다.
s.readable									->읽기 스트림이고 열린 상태라면 true
s.pause();									->"data" 이벤트를 일시 중단한다. 예) 업로드 속도 제어
s.resume();									->이벤트 재개

//만약 "data" 이벤트 핸들러에 문자열을 전달하고 싶다면 인코딩을 지정한다.
s.setEncoding(enc);							->바이트 값을 어떻게 디코딩 할 것인가?
											->"utf8"이나 "ascii" 또는 "base64"
```
앞의 코드에서 보았듯이, 노드 스트림은 바이너리 데이터와 텍스트 데이터를 모두 처리할 수 있다. 텍스트는 일반적인 자바스크립트 문자열을 사용하여 전송되고, 바이트는 노드에만 있는 전용 형식인 버퍼(Buffer)를 사용하여 처리된다. 노드 버퍼는 고정 길이의 유사 배열 객체로, 각 요소는 0과 255 사이의 숫자여야 한다. 노드 프로그램은 버퍼를 데이터의 덩어리로 취급하는데, 하나의 스트림에서 데이터를 버퍼로 읽고 다른 스트림에 버퍼의 내용을 쓴다.
하지만 버퍼의 각 바이트는 배열 원소와 같은 방법으로 접근될 수 있으며, 버퍼에는 한 버퍼에서 다른 바퍼로 바이트를 복사하는 메서드, 버퍼의 특정 부분을 추출하는 메서드, 특정 인코딩을 적용해서 문자열을 버퍼에 쓰는 메서드, 버퍼의 전부 또는 일부를 문자열로 디코딩 하는 메서드 등이 준비되어 있다.
```
var bytes = new Buffer(256);				->256바이트 버퍼를 만든다.
for(var i = 0; i < bytes.length; i++)		->인덱스를 통해 루프를 수행
	bytes[i] = i;							->버퍼의 각 요소를 설정한다.
var end = bytes.slice(240,256);				->버퍼의 특정 부분에 대한 뷰를 만든다.
end[0]										->240: end[0]은 bytes[240]이다.
end[0] = 0;									->특정 부분의 요소를 수정한다.
bytes[240]									->0: 원래 버퍼도 변경된다.
var more = new Buffer(8);					->별도의 버퍼를 만든다.
end.copy(more, 0, 8, 16);					->end[]의 8-15 요소를 more[]에 복사한다.
more[0]										->248

//버퍼는 또한 바이너리 <=> 텍스트 변환도 수행한다.
//유효한 인코딩은 "utf8", "ascii", "base64"이고, 기본 값은 "utf8"이다.
var buf = new Buffer("2πr", "utf8");		->UTF-8을 사용하여 텍스트를 바이트로 인코딩 한다.
buf.length									->세 글자 4바이트다.
buf.toString()								->"2πr": 텍스트로 다시 변환한다.
buf = new Buffer(10);						->고정된 길이의 버퍼
var len = buf.write("2πr", 4);				->4번째 바이트 위치에 텍스트를 쓴다.
buf.toString("utf8", 4, 4+len)				->"2πr": 특정 범위의 바이트를 디코딩한다.
```
노드의 파일과 파일 시스템 API는 "fs"모듈에 있다.
```
var fs = require("fs");				->파일 시스템 API를 불러온다.
```
이 모듈은 대부분의 메서드에 대해 동기 버전도 함께 제공한다. 이름이 'Sync'로 끝나는 메서드는 결과 값을 반환하거나 예외를 발생시키는 블로킹 메서드다. 이름이 'Sync'로 끝나지 않는 파일 시스템 메서드는 사용자가 지정한 콜백 함수로 결과 값이나 에러를 전달한다.
다음 코드는 블로킹 메서드를 사용하여 텍스트 파일을 읽고 논블로킹 메서드를 사용하여 바이너리 파일을 읽는 예제다.
```
//동기적으로 파일을 읽는다. 바이트 대신 텍스트를 얻으려 인코딩을 지정한다.
var text = fs.readFileSync("config.json", "utf8");

//비동기적으로 바이너리 파일을 읽는다. 데이터를 얻기 위한 콜백 함수를 전달한다.
fs.readFile("image.png", function(err,buffer) {
	if (err) throw err;				->무언가 잘못 되었다.
    process(buffer);				->파일 내용은 buffer에 있다.
});
```
비슷한 함수 writeFile()과 writeFileSync()는 파일에 쓰기 작업을 한다.
```
fs.writeFile("config.json", JSON.stringify(userprefs));
```
앞서 나온 함수들은 파일의 내용을 하나의 문자열이나 버퍼로 취급했다. 그러나 노드에는 파일을 읽고 쓰기 위한 용도의 스트리밍 API도 있다. 다음 함수는 한 파일을 다른 파일로 복소한다.
```
//스트리밍 API로 파일 복사하기. 완료 시점을 알고 싶으면 콜백 함수를 전달하면 된다.
function fileCopy(filename1, filename2, done) {
	var input = fs.createReadStream(filename1);
    var output = fs.createWriteStream(filename2);
    
    input.on("data", function(d) { output.write(d); });
    input.on("error", function(err) { throw err; });
    input.on("end", function() {
    	output.end();
        if (done) done();
    });
}
```
또한 "fs" 모듈에는 디렉터리 목록을 나열하거나, 파일 속성을 질의하는 동의 메서드도 포함되어 있다. 다음 노드 프로그램은 파일 크기와 수정일자에 따라 디렉터리 목록을 출력하고 이를 위해 동기 메서드를 사용한다.
```
#! /usr/local/bin/node
var fs = require("fs"), path = require("path");						->필요한 모듈을 불러온다.
var dir = process.cwd();											->현재 디렉터리
if (process.argv.length > 2) dir = process.argv[2];					->또는 명령줄로부터 얻는다.
var files = fs.readdirSync(dir);									->디렉터리 내용을 읽는다.
process.stdout.write("Name\tSize\tDate\n");							->헤더를 출력한다.
files.forEach(function(filename) {									->각 파일 이름에 대해
	var fullname = path.join(dir, filename);						->디렉터리와 이름을 합치고
    var stats = fs.statStnc(fullname);								->파일속성을 얻는다.
    if (stats = fs.statSync(fullname)) filename += "/";				->하위 데럭터리 표시
    process.stdout.write(filename + "\t" + 							->파일 이름을 출력하고
    					stats.size + "\t" + 						->파일 크기를 덧붙인고
                        state.mtime + "\n");						->수정일자도 덧붙인다.
});
```
제일 앞줄에 있는 #! 주석을 살펴보라. 이것은 유닉스의 "shebang" 주석이며, 스크립트 파일을 실행할 인터프리터를 지정함으로써 해당 스크립트 파일이 스스로 실행될 수 있도록 한다. 파일의 가장 첫 줄에 이런 내용이 있다면 노드는 첫 줄을 무시할 것이다.
"net" 모듈은 TCP 기반 네트워킹 API다. (데이터그램 기반 네트워킹에 대해서는 "dgram" 모듈을 참고하라.) 다음은 노드로 구축한 아주 간단한 TCP서버다.
```
//노드로 구현한 간단한 TCP 에코 서버. 2000번 포트에서 연결을 수신하고
//클라이언트에게서 온 데이터를 다시 돌려보낸다.
var net = require('net');
var server = net.createServer();
server.listen(2000, function() { console.log("2000qjs 포트에서 수신 중"); });
server.on("connection", function(stream) {
	console.log("다음의 연결을 수락함: ", stream.remoteAddress);
    stream.on("data", function(data) { stream.write(data); });
    stream.on("end", function(data) { console.log("연결 닫힘"); });
});
```
기본 "net" 모듈 외에도 노드는 내장된 "http"모듈을 통해 HTTP 프로토콜을 지원하고 있다. 다음 예제에서 좀 더 자세히 다루자.
#####1.노드 예제: HTTP 서버
이 서버는 현재 디렉터리의 파일을 제공하고 또한 특별한 목적을 지닌 두 URL을 구현한다. 이 서버는 노드의 "http"모듈과 앞에서 다룬 파일 API와 스트림 API를 사용한다.
```
//이것은 간단한 NODEJS HTTP 서버로 현재 디렉터리의 파일을 제공하며
//테스트를 위한 특별한 두 가지 URL을 구현한다.
//http://localhost:8000이나 http://127.0.0.1:8000를 통해 서버에 연결할 수 있다.

//먼저, 사용할 모듈을 불러온다.
var http = require('http');
var fs = require('fs');

var server = new http.Server();
server.listen(8000);

//노드는 이벤트 핸들러를 등록하기 위해 "on()" 메서드를 사용한다.
//서버가 새로운 요청을 받으면, 요청을 처리하기 위해 이 함수를 실행한다.
server.on("request", function (request, response) {
	//요청 URL을 분석한다.
    var url = require('url').parse(request.url);
    
    //응답을 보내기 전에 잠시 대기하는 URL
    //이는 느린 네트워크 연결을 시뮬레이션 하는 데 유용하다.
    if(url.pathname === "/test/delay") {
    	//쿼리 문자열의 지연 값을 사용하거나 기본으로 2000밀리초를 지정한다.
        var delay = parseInt(url.query) || 2000;
        //응답 상태 코드와 헤더를 설정한다.
        response.writeHead(200, {"Content-Type": "text/plain; charset=UTF-8"});
        //응답 본문을 출력한다.
        response.write("Sleeping for " + delay + "milliseconds...");
        //그리고 setTimeout을 통해 나중에 호출되는 함수에서 응답을 종료하게 한다.
        setTimeout(function() {
        	response.write("done.");
            response.end();
        }, delay);
    }
    //요청 URL이 "/test/mirror"라면, 요청을 그대로 다시 돌려 보낸다.
    //요청 헤더와 본문을 보고자 할 때 유용하다.
    else if (url.pathname === "/test/mirror") {
    	//응답 상태와 헤더
        response.writeHead(200, {"Content-Type": "text/plain; charset=UTF-8"});
        //응답 본문을 요청 내용으로 쓰기 시작.
        response.write(request.method + " " + request.url + "HTTP/" + request.httpVarsion + "\r\n");
        //요청 헤더
        for(var h in request.headers) {
        	response.write(h + ": " + request.headers[h] + "\r\n");
        }
        response.write("\r\n");									->빈 줄을 추가하여 헤더 출력을 끝냄
        //이벤트 핸들러 함수에서 응답을 완료함.
        //요청 본문의 청크를 수신하는 대로, 응답에 추가한다.
        request.on("data", function(chunk) { response.write(chunk); });
        //요청이 끝에 이르면, 응답 역시 완료된다.
        request.on("end", function(chunk) { response.end(); });
    }
    //그렇지 않으면 로컬 디렉터리의 파일을 제공한다.
    else {
    	//로컬 파일 이름을 얻고 확장자를 기반으로 콘텐츠 형식을 정한다.
        var filename = url.pathname.substring(1);						->제일 앞의 슬래시를 제거
        var type;
        switch(filename.substring(filename.lastIndexOf(".")+1)) {		->확장자
        	case "html":		
            case "htm":			type = "text/html; charset=UTF-8; break;
            case "js":			type = "application/javascript; charset=UTF-8"; break;
            case "css":			type = "text/css; charset=UTF-8"; break;
            case "txt":			type = "text/plain; charset=UTF-8"; break;
            case "manifest":	type = "text/cache-manifest; charset=UTF-8"; break;
            default:			type = "application/octet-stream"; break;
        }
        
        //비동기적으로 파일을 읽고, 읽은 내용을 콜백 함수에 단일 청크로 전달한다.
        //매우 큰 파일에 대해서는, fs.createReadStream()과 스트리밍 API를 사용하는 편이 더 좋다.
        fs.readFile(filename, function(err, context) {
        	if(err) {													->어떠한 이유로 파일을 읽을 수 없다면
            	response.writeHead(404, {								->404 Not Foun 상태를 전송
                	"Content-Type": "Text/plain; charset=UTF-8"
                });
                response.write(err.message);							->간단한 에러 메시지 본문
                response.end();											->완료
            }
            else {														->아니면, 파일을 정상적으로 읽었다.
            	response.writeHead(200, {"Content-Type": type});		->상태 코드와 MIME 형식을 설정한다.
                response.write(content);								->파일 내용을 응답 본문으로 보낸다.
                reponse.end();											->완료
            }
        });
    }
});
```
#####2.노드 예제: HTTP 클라이언트 유틸리티 모듈
HTTP GET과 POST 요청을 보내는 유틸리티 함수를 정의하려고 "http" 모듈을 사용한다. 예제는 "httputils" 모듈로 구조화 되었고, 다음과 가팅 코드에서 사용할 수 있다.
```
var httputiles = require("./httputils");				->".js" 접미사가 없는 것에 유의
httputils.get(url, function(status, headers, body) { console.log(body); });
```
require() 함수는 모듈 코드를 실행할 때 eval()을 사용하지 않는다. 모듈 코드는 어떤 전역 변수도 정의할 수 없고 전역 네임스페이스를 젼경할 수도 없는 특별한 환경에서 해석되고 처리된다. 이 특별한 환경에는 exports라는 이름을 가진 전역 객체가 존재한다. 모듈은 바로 이 객체에 프로퍼티를 정의함으로써 API를 외부에 노출할 수 있다.
```
//노드에서 사용할 수 있는 httputils 모듈

//지정된 URL에 대해 비동기 HTTP GET 요청을 전송하고,
//HTTP 상태, 헤더, 응답본문을 지정된 콜백 함수에 전달한다.
//exports 객체를 통해 어떻게 이 메서드를 노출하는지 주의 깊게 살펴보라.
exports.get = function(url, callback) {
	//URL을 분석하고 필요한 부분을 얻는다.
    url = require('url').parse(url);
    var hostname = url.hostname, port = url.port || 80;
    var path = url.pathname, query = url.query;
    if(query) path += "?" + query;
    
    //간단한 GET 요청을 생성한다.
    var client = require("http").createClient(port, hostname);
    var request = client. request("GET", path, {
    	"HOST": hostname										->요청 헤더
    });
    request.end();
    
    //응답을 처리할 함수.
    request.on("response", function(response) {
    	//응답 본문을 바이트가 아니라 텍스트로 얻으려 인코딩을 지정함.
        response.setEncodin("utf8");
        //응답 본문을 저장한다.
        var body = ""
        response.on("data", function(chunk) { body += chunk; });
        //응답이 완료되면 콜백 함수를 호출한다.
        response.on("end", function() {
        	if(callback) callback(response.statusCode, response.headers, body);
        });
    });
};
//요청 본문에 데이터를 포함한 간단한 HTTP POST 요청
exports.post = function(url, data, callback) {
	//URL을 분석하고 필요한 부분을 얻는다.
    url = require('url').parse(url);
    var hostname = url.hostname, post = url.port || 80;
    var path = url.pathname, query = url.query;
    if(query) path += "?" + query;
    
    //요청 본문으로 보낼 데이터의 형식을 판단함.
    var type;
    if(data == null) data = "";
    if(data instanceof Buffer)										->바이너리 데이터
    	type = "application/octet-stream";
    else if(typeof data === "string")								->문자열 데이터
    	tpye= "test/plain; charset=UTF-8";
    else if(typeof data === "object"){								->이름 = 값 쌍
    	data = require("querystring").stringify(data);
        type = "application/x-www-form-urlencoded";
    }
    //요청 본문을 포함한 POST 요청을 생성한다.
    var client = require("http").createClient(port, hostname);
    var request = client.request("POST", path, {
    	"HOST": hostname,
        "Content-Type": type
    });
    request.write(data);											->요청 본문을 보내고
    request.end();
    request.on("response", function(response) {						->응답을 처리함.
    	response.setEncoding("utf8");								->응답 내용이 텍스트라고 가정
        var body = "";												->응답 본문을 저장하는 변수
        response.on("data", function(chunk) { body += chunk; });
        response.on("end", function() {								->완료되면 콜백을 호출한다.
        	if(callback) callback(response.statusCode, response.headers, body);
        });
    });
};
```