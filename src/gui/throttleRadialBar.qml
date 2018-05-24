import QtQuick 2.4
import SDK 1.0
import QtQuick.Layouts 1.1


Rectangle {
    id: root
    Layout.alignment: Layout.Center
    width: 160
    height: 145
    color: "#181818"
    property var suffix: "%"
    property int minVal: 0
    property int maxVal: 100
    property var actVal: 0

    Connections{
        target: throttleWidget
        onRandomValueChanged: root.actVal = throttleWidget.randomValue
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

    Rectangle {
            Layout.alignment: Layout.Center
            width: 160
            height: 145
            color: "#181818"
    Text {
        id: name
        text: "Throttle"
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
        progressColor: "#6affcd"
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
        textColor: "#00ffc1"
    }}
}
