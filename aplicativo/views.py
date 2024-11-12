from django.shortcuts import render, redirect
from teste.forms import UsuarioForm, TarefaForm
from teste.models import usuarios, tarefas

def lista_usuarios(request):
    usuarios_list = usuarios.objects.all()
    return render(request, 'usuarios/lista.html', {'usuarios': usuarios_list})

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/cadastrar.html', {'form': form})


def lista_tarefas(request):
    tarefas_list = tarefas.objects.all()
    return render(request, 'tarefas/lista.html', {'tarefas': tarefas_list})

def atualizar_usuario(request, usuario_id):
    usuario = usuarios.objects.get(pk=usuario_id)
    if request.method == 'POST':
        usuario.u_nome = request.POST['u_nome']
        usuario.u_email = request.POST['u_email']
        usuario.save()
        return redirect('lista_usuarios')  # Redirecionar para a lista de usuários
    else:
        context = {'usuario': usuario}
        return render(request, 'usuarios/atualizar.html', context)

def deletar_usuario(request, usuario_id):
    usuario = usuarios.objects.get(pk=usuario_id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuarios')
    else:
        context = {'usuario': usuario}
        return render(request, 'usuarios/confirmar_delecao.html', context)

def cadastrar_tarefa(request):
    if request.method == 'POST':
        form = tarefas.objects.create(
            t_codigo=request.POST['t_codigo'],
            t_setor=request.POST['t_setor'],
            usuario=usuarios.objects.get(u_codigo=request.POST['usuario'])
        )
        form.save()
        return redirect('lista_tarefas')
    else:
        return render(request, 'tarefas/cadastrar.html', {'form': tarefas})