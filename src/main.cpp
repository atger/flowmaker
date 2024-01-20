#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QQuickWindow>
#include <QDir>
#include <QModelIndex>
#include <QQmlContext>
#include <QFileSystemModel>

int main(int argc, char** argv) {
    QGuiApplication app(argc, argv);
    QQmlApplicationEngine engine;
    QFileSystemModel model;
    QModelIndex index = model.setRootPath(QDir::homePath());
    QQmlContext *rootContext = engine.rootContext();
    rootContext->setContextProperty("systemModel", &model);
    engine.load(QUrl("qrc:/qml/main.qml"));
    app.exec();
}