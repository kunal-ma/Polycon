<div align="center">
<h1 align="center">Polycon</h1>

<p align="center">
Customizable and lightweight icon pack template for Android, built using Kotlin. 
<br />
<br />
<a href="#getting-started">Getting Started</a>
·
<a href="https://github.com/kunal-ma/Polycon/issues">Issue Tracker</a>
·
<a href="#roadmap">Project Roadmap</a>
</p>
</div>

## Getting Started

You can download pre-built APKs, which include my curated selection of icons, from the [Releases](https://github.com/kunal-ma/Polycon/releases) page. Alternatively, you can build the project yourself and customize the icons to suit your preferences.

## Building the Project

> [!WARNING]
> Please note that the following steps have been simplified for clarity. It is crucial to follow them **precisely** to prevent any potential issues. Names and file paths must be **accurate** and the format of the files must be maintained to ensure the project builds correctly.

### Clone the repo or download the [ZIP file](https://github.com/kunal-ma/polycon/archive/refs/heads/main.zip).

```sh
git clone https://github.com/kunal-ma/polycon.git
```

### Customizing the Icons

- The icons must follow the following parameters:
  - The icon must be square in shape.
  - The icon must be in PNG format.
  - The icon must be 192x192 pixels in size.
  
- The icons must be named according to the following convention:
  - Lowercase letters only (e.g., `clock.png`)
  - To add spaces, use underscores (e.g., `google_pay.png`)

**Note** : To get icons from other icon packs, refer to the [Extraction Guide](https://github.com/kunal-ma/Polycon/blob/main/scripts/Extraction.md).

### Updating the XML Files

Icon packs offer the ability to group icons into categories. This helps users make sense of the icons and find them easily. To update the XML files, follow these steps:

- **Option 1** : You can manually update the XML files to reflect the changes made to the icons. For example, the `Apps` group contains the `google_pay.png` and `clock.png` icons. The folders and XML files are updated as follows:

  - Move the icons to the `app/src/main/res/drawable` directory. **Do not** create subdirectories within the `drawable` directory.

  - Update the `app/src/main/res/xml/drawable.xml` file:
  
    ```xml
    <!-- Add the group name to the category title -->
    <!-- Add icon entries under the category tag -->
    <!-- Leave a line between groups -->
    <category title="Apps" />
    <item drawable="google_pay" />
    <item drawable="clock" />
    ```

  - Update the `app/src/main/res/values/icon_pack.xml` file:

    ```xml
    <!-- Add all group name entries in the icon_pack array -->
    <string-array name="icon_pack"> 
        <item>Apps</item>
    </string-array>

    <!-- Add the icon entries to the respective group array -->
    <string-array name="Apps">
        <item>google_pay</item>
        <item>clock</item>
    </string-array>
    ```

> [!IMPORTANT]
> The following method implements a script and requires Python to be installed on your system, and available in your PATH.

- **Option 2** : The `icon_list.py` script automates the process of updating the necessary folders and XML files to reflect the changes made to the icons. To use the script, follow these steps:

  - Add, remove or replace the icons to the `icons` directory. To group the icons, you can create subdirectories within the `icons` directory. The **names of the subdirectories** will be used as the **group names** in the icon pack.
  
    As an example, my curated selection of icons are organized into folders such as `Apps`, `Games`, etc. However, **do not** make subdirectories within the subdirectories.

  - Run the following script via the terminal in the **root directory** of the project:

    ```sh
    python scripts/icon_list.py
    ```

### Compiling the APK

> [!IMPORTANT]
> The following method requires [Android Studio](https://developer.android.com/studio) with the Android SDK installed, as well as [keystores](https://developer.android.com/studio/publish/app-signing#generate-key) for signing the APK.

- **Option 1** : You can build the APK using Android Studio. To do this, perform the following steps:
  
  - Open the project in Android Studio and finish syncing the project.
  
  - Build the project using the `Build > Generate Signed Bundle / APK` option. More information can be found [here](https://developer.android.com/studio/publish/app-signing#sign_release).

  - The APK will be generated in the `app/release` directory.

<br />

- **Option 2** : You can build the APK using the Gradle build system. To do this, perform the following steps:

    - Modify and add the following to `gradle.properties` file in the root directory of the project :
  
      ```gradle
      RELEASE_STORE_FILE= // path to your keystore
      RELEASE_STORE_PASSWORD= // store password
      RELEASE_KEY_ALIAS= // alias
      RELEASE_KEY_PASSWORD= // password
      ```

    - Add the following to the `app/build.gradle.kts` file in the `android` block:
  
      ```gradle
      signingConfigs {
          release {
              storeFile file(RELEASE_STORE_FILE)
              storePassword RELEASE_STORE_PASSWORD
              keyAlias RELEASE_KEY_ALIAS
              keyPassword RELEASE_KEY_PASSWORD
          }
      }
      buildTypes {
          release {
              signingConfig signingConfigs.release
          }
      }
      ```
    
    - Open the terminal in the root directory of the project, and run the following command:
  
      ```sh
      ./gradlew assembleRelease
      ```
    
    - The APK will be generated in the `app/build/outputs/apk/release` directory.

### Installation

Transfer the APK generated in the previous step, or downloaded from the Releases page, to your Android device. Install the APK on your device by opening the file in a file manager and following the on-screen instructions.

> [!NOTE]
> You may need to enable the installation of apps from unknown sources in your device settings. Moreover, Google Play Protect may warn you about the APK, as it is not available on the Play Store. You can safely ignore this warning and install the APK.

## Roadmap

- [ ] Splash Screen
- [ ] Icon Search
- [ ] Dashboard
  - [ ] Icon Request
  - [ ] Icon Counter
  - [ ] Light/Dark Mode

## Acknowledgements

Distributed under the GNU General Public License v3.0. See `LICENSE` for more information.

Any contributions you make are **greatly appreciated**. If you have a suggestion that would make this better, please fork the repo and create a pull request. Thanks again :)