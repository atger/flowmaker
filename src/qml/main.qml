import QtQuick
import QtQuick.Controls

ApplicationWindow {
    visible: true
    
    // title of the application
    title: qsTr("FlowMaker")
    width: 900
    height: 600

    // Content Area
    Text {
        anchors.centerIn: parent
        text: "FlowMaker"
    }
}