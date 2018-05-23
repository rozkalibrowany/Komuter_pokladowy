import QtQuick 2.4
import SDK 1.0
import QtQuick.Layouts 1.1


Rectangle {
    id: root
    Layout.alignment: Layout.Center

    height: 145
    width: 160
    color: "#181818"
    property var suffix: "°"
    property int minVal: 0
    property int maxVal: 100
    property var actVal: 0
    property int widthRadial: 160

    Connections{
        target: contrTempWidget
        onRandomValueChanged: root.actVal = contrTempWidget.randomValue
    }

    function getWidth() {
        var calcWidth = width / 1.4
        if (calcWidth >= 114.285) {
            calcWidth = calcWidth - (0.00000001)*actVal
        } else
        {
            calcWidth = 114.285
        }
        return calcWidth
    }

    function getProgressColor() {
        var pColor

        if (actVal <= 40) {
            pColor = "#6affcd"
        } else if (actVal <= 60){
            pColor = "#ffff99"
        } else {
            pColor = "#ff4d4d"
        }
        return pColor
    }

    function getFontColor() {
        var pColor

        if (actVal <= 40) {
            pColor = "#00ffc1"
        } else if (actVal <= 60){
            pColor = "#ffff99"
        } else {
            pColor = "#ff4d4d"
        }
        return pColor
    }

    Rectangle {
            Layout.alignment: Layout.Center
            width: 160
            height: 145
            color: "#181818"
    Text {
        id: name
        text: "Controller Temp"
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: parent.top
        anchors.topMargin: 5
        font.pointSize: 13
        color: "#00ffc1"
    }

    RadialBar {
        id: rb
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.bottom: parent.bottom
        width: getWidth()
        height: width
        penStyle: Qt.RoundCap
        progressColor: getProgressColor()
        foregroundColor: "#191a2f"
        dialWidth: 11 // szerokość paska postępu
        minValue: minVal
        maxValue: maxVal
        value: actVal
        suffixText: suffix
        //dialType: RadialBar.DialType.MinToMax
        textFont {
            family: "Halvetica"
            italic: false
            pointSize: 18
        }
        textColor: getFontColor()
    }}
}
