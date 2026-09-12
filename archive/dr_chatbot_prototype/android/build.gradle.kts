
allprojects {
    repositories {
        google()
        mavenCentral()
    }
}

buildscript {
    repositories {
        google()
        mavenCentral()  /
    }
    dependencies {

        classpath("com.android.tools.build:gradle:7.4.1")


        classpath("com.google.gms:google-services:4.3.15")
    }
}

subprojects {

    project.evaluationDependsOn(":app")
}

tasks.register<Delete>("clean") {
    delete(rootProject.layout.buildDirectory)
}
