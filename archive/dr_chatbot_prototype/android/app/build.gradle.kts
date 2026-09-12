plugins {
    id("com.android.application")
    kotlin("android")
}

android {
    compileSdkVersion(33)

    defaultConfig {
        applicationId = "com.yourcompany.drchatbot"  // Set your app's package name (unique ID)
        minSdkVersion(21)  // Set the minimum SDK version (adjust as per your app's requirement)
        targetSdkVersion(33)  // Set the target SDK version (adjust as per your app's requirement)
        versionCode = 1  // Set version code
        versionName = "1.0"  // Set version name
    }

    buildTypes {
        // Define build types (debug and release)
        getByName("release") {
            isMinifyEnabled = false  // Set to true if you want to enable Proguard for release builds
            proguardFiles(getDefaultProguardFile("proguard-android-optimize.txt"), "proguard-rules.pro")
        }
    }

    // Set up Kotlin-specific configurations
    kotlinOptions {
        jvmTarget = "1.8"  // Set JVM target to 1.8 (or as per your requirements)
    }
}

dependencies {
    // Firebase dependencies for authentication and Firestore
    implementation("com.google.firebase:firebase-auth:21.0.5")  // Firebase Authentication
    implementation("com.google.firebase:firebase-firestore:24.0.0")  // Firestore for database

    // Firebase Core library for initializing Firebase services
    implementation("com.google.firebase:firebase-core:21.1.0")

    // Firebase Messaging (optional) for push notifications, if needed
    implementation("com.google.firebase:firebase-messaging:23.1.0")

    // Kotlin standard library for Android
    implementation("org.jetbrains.kotlin:kotlin-stdlib:1.6.10")

    // AndroidX dependencies (replace versions as per your requirements)
    implementation("androidx.core:core-ktx:1.6.0")
    implementation("androidx.appcompat:appcompat:1.3.1")
    implementation("com.google.android.material:material:1.4.0")

    // Other dependencies as needed
    // implementation("com.squareup.retrofit2:retrofit:2.9.0")  // For API calls, if needed
    // implementation("com.squareup.okhttp3:okhttp:4.9.1")  // For networking, if needed
}

apply(plugin = "com.google.gms.google-services")
