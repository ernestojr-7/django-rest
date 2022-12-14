from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []


class ListaMatriculaAlunoSerializer(serializers.ModelSerializer):
    # para aparecer descricao do curso em vez do id
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()


class ListaAlunoMatriculadosEmUmCursoSerializer(serializers.ModelSerializer):
    # para aparecer descricao do aluno em vez do id
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')

    class Meta:
        model = Matricula
        fields = ['aluno_nome']
