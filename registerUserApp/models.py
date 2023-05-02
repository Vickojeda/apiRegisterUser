# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from datetime import date
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Boleta(models.Model):
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto', blank=True, null=True)
    rut_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='rut_usuario')
    numero_boleta = models.BigIntegerField(primary_key=True)
    total_boleta = models.CharField(max_length=20)
    cant_producto = models.BigIntegerField()
    created_at = models.DateField()
    update_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'boleta'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DulcetulipanesUsuarios(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    apellido = models.CharField(max_length=30, blank=True, null=True)
    direccion = models.CharField(max_length=20, blank=True, null=True)
    rut = models.CharField(max_length=20, blank=True, null=True)
    numero_telefono = models.BigIntegerField()
    mail = models.CharField(max_length=20, blank=True, null=True)
    contrasena = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(default=date.today)
    updated_at = models.DateTimeField(default=date.today)

    class Meta:
        managed = False
        db_table = 'dulcetulipanes_usuarios'


class HistorialBoleta(models.Model):
    id_historia = models.BigIntegerField(primary_key=True)
    numero_boleta = models.ForeignKey(Boleta, models.DO_NOTHING, db_column='numero_boleta', blank=True, null=True)
    created_at = models.DateField()
    update_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'historial_boleta'


class Producto(models.Model):
    id_producto = models.CharField(primary_key=True, max_length=20)
    nombre_producto = models.CharField(max_length=20)
    precio = models.BigIntegerField()
    descripcion_producto = models.CharField(max_length=30, blank=True, null=True)
    created_at = models.DateField()
    update_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'producto'


class Rol(models.Model):
    id_rol = models.BigIntegerField(primary_key=True)
    descripcion_rol = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateField()
    update_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'rol'


class StockProducto(models.Model):
    id_producto = models.CharField(primary_key=True, max_length=20)
    cantidad_producto_stock = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateField()
    update_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'stock_producto'


class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=20)
    rut_usuario = models.CharField(primary_key=True, max_length=20)
    numero_telefono = models.CharField(max_length=20)
    mail = models.CharField(max_length=20)
    contrasena = models.CharField(max_length=20)
    id_rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='id_rol')
    created_at = models.DateField(default=date.today)
    update_at = models.DateField(default=date.today)

    class Meta:
        managed = False
        db_table = 'usuario'
