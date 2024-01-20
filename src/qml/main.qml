import QtQuick
import QtQuick.Layouts
import QtQuick.Controls

ApplicationWindow {
    id: window
    width: 900
    height: 600
    title: qsTr("FlowMaker")
    visible: true
    
    menuBar: MenuBar {
        Menu {
            title: qsTr("&File")
            Action { text: qsTr("&New") }
            Action { text: qsTr("&Open") }
            Action { text: qsTr("&Save") }
            Action { text: qsTr("Save &As") }
        }
        Menu {
            title: qsTr("&Edit")
            Action { text: qsTr("Cu&t") }
            Action { text: qsTr("&Copy") }
            Action { text: qsTr("&Paste") }
        }
        Menu {
            title: qsTr("View")
            Action { text: qsTr("Property Window") }
        }
        Menu {
            title: qsTr("Help")
            Action { text: qsTr("&About") }
        }

    }

    header: ToolBar {
        RowLayout {
            anchors.fill: parent
            ToolButton {
                text: qsTr("‹")
                onClicked: stack.pop()
            }
            Label {
                text: "Editor"
                elide: Label.ElideRight
                horizontalAlignment: Qt.AlignHCenter
                verticalAlignment: Qt.AlignVCenter
                Layout.fillWidth: true
            }
            ToolButton {
                text: qsTr("⋮")
                onClicked: menu.open()
            }
        }
    }

    footer: TabBar {

    }

    // Content Area
    StackView {
        id: stack
        initialItem: mainView
        anchors.fill: parent
    }

    Component {
        id: mainView

        Row {
            spacing: 2
            anchors.fill:parent

            TreeView {
                id: tree
                width: 300
                height: parent.height
                model: systemModel
                delegate: TreeViewDelegate{}
            }
            ScrollView {
                height: parent.height
                anchors.left: tree.right
                anchors.right: parent.right
                
                TextArea {
                    id: editor
                    anchors.fill: parent
                    padding: 10
                    placeholderText: "Write something useful."
                    font.family: "Helvetica"
                    font.pointSize: 12
                    wrapMode: TextEdit.WordWrap
                    color: "white"
                    focus: true
                    background: Rectangle {
                        anchors.fill: parent
                        color: "slategray"
                    }
                }
            }
        }
    }
}