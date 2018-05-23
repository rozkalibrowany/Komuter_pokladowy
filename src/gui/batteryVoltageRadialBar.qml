import QtQuick 2.4
import SDK 1.0
import QtQuick.Layouts 1.1


Rectangle {
    id: root
    Layout.alignment: Layout.Center
    width: 160
    height: 145
    color: "#181818"
    property var suffix: "V"
    property int minVal: 0
    property int maxVal: 102
    property var actVal: 0

    Connections{
        target: batteryVoltageWidget
        onRandomValueChanged: root.actVal = batteryVoltageWidget.randomValue
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

        if (actVal <= 72) { // Po 3V na celę
            pColor = "#ff4d4d"
        } else if (actVal <= 86.4){
            pColor = "#ffff99"
        } else if (actVal <= 91) {
            pColor = "#6affcd"
        } else {
            pColor = "#99ff99"
        }
        return pColor
    }

    function getFontColor() {
        var pColor

        if (actVal <= 72) {
            pColor = "#ff4d4d"
        } else if (actVal <= 86.4){
            pColor = "#ffff99"
        } else if (actVal <= 91) {
            pColor = "#00ffc1"
        } else {
            pColor = "#99ff99"
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
        text: "Battery Voltage"
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: parent.top
        anchors.topMargin: 5
        font.pointSize: 13
        color: "#00ffc1"
    }

    RadialBar {
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
