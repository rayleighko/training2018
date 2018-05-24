## Android Studio & OpenCV 연동하기  

##### 

[뒤로가기](/opencv/README.md)

Android Studio와 OpenCV 3.3.0을 연동해보도록 하자.  

만약 Android Studio가 Cmake를 지원하지 않았다면, NDK를 추가하기위해 ndk-build를 사용했겠지만 이제는 지원하므로, 우리는 Cmake를 사용하여 연동해보도록 하자.  

---

우선 필자는 최대한 최신 버전을 사용하려고 했다. 그래서 이번 예제에서 필요한 것은 아래와 같다.  

또한, 모든 예제는 [여기][opencvblog]를 참고했다.  

* [windows 10][windows10]
* [Android-OpenCV 3.3.0][android-opencv]
* [Android Studio 2.3.3][androidstudio]
* [Cmake 3.9.1][cmake]
* Android 8.0(API 26)
  

다운로드나 설치 방법에 대한 설명은 너무 많으니 여기서는 간단하게 연동해서 사용해보는 예제까지만 진행하려고 한다.  

그리고 정리하는 차원에서 사진보다는 글이 많은 예제가 될 것이니, 그림이 익숙하다면 다른 블로그를 활용하기 바란다.  

우선 프로젝트를 생성해보자. 프로젝트 생성 시 **New project**를 누르고 아래의 체크 박스인 **Include C++ support**를 선택해주도록 하자.  

또한, **Minimum SDK**를 API14로 설정해주자. 이는 **appcompat-v7 라이브러리**를 사용하기 위함이다.  

* Include c++ support 선택
* Minimum SDK를 API 14로 설정
* Empty Activity
* 이후 체크박스 모두 선택

여기까지 진행했으면 이제 [이 곳][tutorial]에서 아래의 과정(링크의 소제목)을 수행하고, 따라오도록 하자.  

* NDK 및 빌드 도구 다운로드
* C/C++ 지원 기능을 활용하여 새 프로젝트 생성
  

이 과정을 끝냈다면, 프로젝트에 OpenCV 라이브러리를 추가해보도록 하자. 우선 [Android-OpenCV 3.3.0][android-opencv]에서 opencv-3.3.0-android-sdk.zip을 받아 압축을 해제한다(필자의 경우 C:\에 해제했다).  

그럼 이제 안드로이드 스튜디오 메뉴에서 **File > New > Import Module**을 선택한다.  

그럼 *Source directory*의 경로를 압축해제한 경로의 **src\java**로 선택하도록 한다(필자의 경우에는 C:\OpenCV-android-sdk\sdk\java 이다).  

* [Android-OpenCV 3.3.0][android-opencv] opencv-3.3.0-android-sdk.zip 압축해제
* Imort Module에서 경로를 압축해제한 경로의 src\java로 설정
* 추가적으로 Android 4.0(API 14) SDK Platform 패키지를 설정하라는 에러가 나오면 클릭하여 설치해서 최신 SDK로 변경해주자.

다음으로 app 모듈의 build.gradle의 값을 openCVLibrary330의 build.gradle에 옮기도록 하자. 아래와 같이 말이다(여기서는 Project view가 아닌 Android view의 Gradle Scripts에서 바꾸는 게 헷갈리지 않으니 참고하자).

```
// app

apply plugin: 'com.android.application'

android {
    compileSdkVersion 26			// 이 부분과
    buildToolsVersion "25.0.0"		// 이 부분,
    defaultConfig {
        applicationId "io.github.rjs1197.opencvproject"
        minSdkVersion 14			// 이 부분과
        targetSdkVersion 26			// 이 부분만 옮기면 된다.
        versionCode 1
        versionName "1.0"
        testInstrumentationRunner "android.support.test.runner.AndroidJUnitRunner"
        externalNativeBuild {
            cmake {
                cppFlags "-frtti -fexceptions"
            }
        }
    }
    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
        }
    }
    externalNativeBuild {
        cmake {
            path "CMakeLists.txt"
        }
    }
}
```
  
```
// openCVLibrary330

apply plugin: 'com.android.library'

android {
    compileSdkVersion 14			// 26으로.
    buildToolsVersion "25.0.0"

    defaultConfig {
        minSdkVersion 8				// 14로
        targetSdkVersion 21			// 26으로
    }

    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.txt'
        }
    }
}
```
  
바꾼 후 Sync Now를 꼭 해주도록 하자. 이 과정이 끝났다면 프로젝트의 기본(default) 모듈인 app에서 openCVLibrary330 모듈을 사용할 수 있도록 설정해야 한다.  

* app의 build.gradle과 openCVLibrary330의 build.gradle의 *compileSdkVersion*, *minSdkVersion*, *targetSdkVersion*을 동이하게 설정해주자.
  

다음으로 **File > Project Structure**에 들어가서, **Module > app**을 선택한다. 그러면 여러 상위 탭들이 뜰텐데 그 중에서 **Dependencies**에서 **초록색 +**를 눌러 **Module dependency**를 선택한다.  

그러면 추가했던 openCVLibrary330 모듈이 있고, 이제 이것을 눌르고, OK를 눌러준다.  

그럼 이제 어느정도 설정이 끝났으니 다음으로 넘어가보자.  

* Project Structure > Module > app > Dependencies > 초록색 + > Module dependency로 진입
* openCVLibrary330 클릭 > OK > OK
  

이제 native libs를 안드로이드 프로젝트로 옮겨주도록 하자(필자의 경우 C:\OpenCV-android-sdk\sdk\native에서의 libs 디렉토리).  

이 디렉토리를 안드로이드 프로젝트의 app\src\main에 복사해주고 디렉토리 이름을 JniLibs로 바꿔주자.  

* C:\OpenCV-android-sdk\sdk\native에서의 libs 디렉토리를 안드로이드 프로젝트의 app\src\main에 복사해준다.
* 이름을 JniLibs로 바꿔준다(이는 sdk\native\jni를 활용하기 위함이다. JNI은 2부에서 설명하겠다).
  

[windows10]: http://bit.ly/2uEecag
[android-opencv]: https://github.com/opencv/opencv/releases
[androidstudio]: https://developer.android.com/studio/index.html?hl=ko
[cmake]: https://cmake.org/download/
[tutorial]: https://developer.android.com/studio/projects/add-native-code.html?hl=ko
[opencvblog]: http://webnautes.tistory.com/1054
